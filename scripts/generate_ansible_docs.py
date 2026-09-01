#!/usr/bin/env python3
"""Generate Docusaurus documentation pages for all giftpilz0 Ansible
collections from their role argument specs.

Usage:

    # Use a local clone of the homelab repo (no network required):
    python3 scripts/generate_ansible_docs.py --repo-dir /path/to/homelab

    # Fetch the latest homelab repo from GitHub:
    python3 scripts/generate_ansible_docs.py

    # Point the output somewhere else / only some collections:
    python3 scripts/generate_ansible_docs.py --out /tmp/docs --collections server,general
"""

from __future__ import annotations

import argparse
import io
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

HOMELAB_REPO = "https://github.com/Giftpilz0/homelab"
COLLECTIONS_REL = Path("ansible_collections/giftpilz0")
SITE_ANSIBLE_DIR = Path("docs") / "projects" / "ansible"

TYPE_NAMES = {
    "str": "string",
    "int": "integer",
    "bool": "bool",
    "list": "list",
    "dict": "dict",
}

# Table columns (must stay in sync with the cell-builder below).
HEADER = ["Variable", "Type", "Options", "Default", "Description"]


def _load_yaml() -> Any:
    """Import PyYAML, failing with a helpful message if unavailable."""
    try:
        import yaml  # type: ignore
    except ImportError:
        sys.stderr.write("PyYAML is required. Install it with: pip install pyyaml\n")
        raise
    return yaml


def fetch_homelab(repo: str, repo_dir: str | None) -> Path:
    """Return a path to the homelab repo containing the collections.

    When ``repo_dir`` is given it is used directly (a local checkout).
    Otherwise the repo is shallow-cloned into a temporary directory; the caller
    is responsible for cleaning up when ``repo_dir`` was not given.
    """
    if repo_dir:
        path = Path(repo_dir)
        if not (path / COLLECTIONS_REL).is_dir():
            raise SystemExit(
                f"'{repo_dir}' does not contain {COLLECTIONS_REL}; "
                "pass the homelab checkout root."
            )
        return path

    sys.stderr.write(f"Cloning {repo} ...\n")
    tmp = Path(tempfile.mkdtemp(prefix="generate_ansible_docs_"))
    subprocess.run(
        ["git", "clone", "--depth", "1", "--filter=blob:none", repo, str(tmp)],
        check=True,
        capture_output=True,
    )
    return tmp


def compact_default(value: Any) -> str:
    """Serialize a default value as a compact, single-line markdown string."""
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, str):
        return '""' if value == "" else collapse_ws(value)
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    return str(value)


def collapse_ws(s: str) -> str:
    """Collapse runs of whitespace (incl. embedded newlines) to single spaces."""
    return " ".join(s.split())


def role_title(role: str) -> str:
    """Render a human-friendly title from a snake_case role name."""
    words = role.replace("_", " ").title().split()
    special = {
        "Github": "GitHub",
        "Gitlab": "GitLab",
        "Opencloud": "OpenCloud",
        "Traefik": "Traefik",
        "Vaultwarden": "Vaultwarden",
    }
    return " ".join(special.get(w, w) for w in words)


def collection_title(collection: str) -> str:
    """Render a human-friendly collection name/title."""
    return collection.replace("_", " ").title()


def type_name(opt_type: Any, elements: Any = None) -> str:
    """Render a human-friendly type name."""
    t = TYPE_NAMES.get(str(opt_type), str(opt_type))
    if opt_type == "list" and elements:
        return f"list of {TYPE_NAMES.get(str(elements), elements)}"
    return t


def choices_text(spec: dict[str, Any]) -> str:
    """Return the Options column text for an option, or '---'."""
    if spec.get("type") == "bool":
        return "true, false"
    choices = spec.get("choices")
    if choices:
        return ", ".join(str(c) for c in choices)
    return "---"


def esc(s: str) -> str:
    """Escape characters that would break a markdown table cell.

    Used for content that is not wrapped in a code span.  ``|`` must be escaped
    to keep a cell intact; ``*`` is escaped so the output matches mdformat.
    """
    return s.replace("\\", "\\\\").replace("|", "\\|").replace("*", "\\*")


def esc_code(s: str) -> str:
    """Escape content that is placed inside an inline-code span.

    Inside a code span only the pipe would split the cell; asterisks and other
    markdown syntax are left literal (matching mdformat), and ``*`` is preserved.
    """
    return s.replace("\\", "\\\\").replace("|", "\\|")


def cell_text(value: str) -> str:
    """Render text for a non-variable table cell.

    Cells that contain ``{``/``}`` (e.g. ``{{ ansible_user }}`` in a default, or a
    JSON dict default) are wrapped in inline code.  MDX otherwise tries to parse
    braces as a JS expression and the build fails; mdformat would strip backslash
    escapes, so inline code is the mdformat-safe way to keep braces literal.
    """
    if "{" in value or "}" in value:
        return f"`{esc_code(value)}`"
    return esc(value)


def build_rows(name: str, spec: dict[str, Any]) -> list[list[str]]:
    """Return the table rows for an option (parent + any nested sub-fields).

    The first element of each row is the full variable name; nested fields are
    rendered as ``<parent>.<field>``.
    """
    opt_type = spec.get("type", "str")
    default = spec.get("default")
    desc = collapse_ws(spec.get("description") or "").rstrip(".")

    rows: list[list[str]] = [
        [
            name,
            type_name(opt_type, spec.get("elements")),
            choices_text(spec),
            compact_default(default),
            desc if desc else "---",
        ]
    ]

    # Expand nested dict/list-of-dict options into parent.field rows.
    for sub_name, sub_spec in (spec.get("options") or {}).items():
        sub_desc = collapse_ws(sub_spec.get("description") or "").rstrip(".")
        rows.append(
            [
                f"{name}.{sub_name}",
                type_name(sub_spec.get("type", "str"), sub_spec.get("elements")),
                choices_text(sub_spec),
                compact_default(sub_spec.get("default")),
                sub_desc if sub_desc else "---",
            ]
        )

    return rows


def render_table(top_options: dict[str, Any], defaults: dict[str, Any]) -> str:
    """Render an mdformat-gfm aligned markdown table.

    Defaults are looked up in ``defaults`` first (the argument spec defaults)
    and fall back to the role's ``defaults/main.yaml`` values in ``main_defaults``
    so non-container collections get populated defaults too.
    """
    rows: list[list[str]] = []

    # Only roles with nested options get blank separator rows (to visually
    # group a parent option with its sub-fields).  Flat-only roles get a clean
    # table with no empty rows.
    any_nested = any(bool(spec.get("options")) for spec in top_options.values())

    for name, spec in top_options.items():
        resolved = dict(spec)
        if "default" not in resolved and name in defaults:
            resolved["default"] = defaults[name]
        built = build_rows(name, resolved)
        rows.extend(built)
        if any_nested and resolved.get("options"):
            # Blank separator row groups the parent option and its sub-fields.
            rows.append(["", "", "", "", ""])

    # Render every row's cells to their final form first (variable names in
    # code spans, brace-containing values code-spanned by cell_text), so column
    # widths can be computed from the actual rendered text — matching what
    # mdformat expects.
    ncols = len(HEADER)

    def render_row(row: list[str]) -> list[str]:
        cells = []
        for i in range(ncols):
            if i == 0 and row[i]:
                cells.append(f"`{esc_code(row[i])}`")
            else:
                cells.append(cell_text(row[i]))
        return cells

    rendered = [render_row(row) for row in rows]

    widths = [len(HEADER[i]) for i in range(ncols)]
    for cells in rendered:
        for i in range(ncols):
            widths[i] = max(widths[i], len(cells[i]))

    def fmt_row(cells: list[str]) -> str:
        padded = [cells[i].ljust(widths[i]) for i in range(ncols)]
        return "| " + " | ".join(padded) + " |"

    sep = ["-" * max(widths[i], 1) for i in range(ncols)]
    out = [fmt_row(HEADER), "| " + " | ".join(sep) + " |"]
    out.extend(fmt_row(cells) for cells in rendered)

    return "\n".join(out)



def render_role_page(collection: str, role: str, spec: dict[str, Any], defaults: dict[str, Any]) -> str:
    """Render the full markdown page for a single role."""
    main = spec.get("argument_specs", {}).get("main", {})
    options = main.get("options", {}) or {}
    short = (main.get("short_description") or "").strip()

    title = role_title(role)
    lines: list[str] = []
    lines.append("---")
    lines.append(f"title: {title} Role")
    lines.append("---")
    lines.append("")

    if short:
        lines.append(short)
        lines.append("")

    lines.append("______________________________________________________________________")
    lines.append("")
    lines.append("## Variables")
    lines.append("")
    if options:
        lines.append(render_table(options, defaults))
    else:
        lines.append("This role takes no variables.")
    lines.append("")

    return "\n".join(lines)


def render_collection_page(collection: str, description: str, roles: list[str]) -> str:
    """Render a collection landing page."""
    lines: list[str] = []
    lines.append("---")
    lines.append(f"title: {collection_title(collection)} Collection")
    lines.append("---")
    lines.append("")
    lines.append(description or f"Ansible collection: {collection}.")
    lines.append("")
    lines.append("______________________________________________________________________")
    lines.append("")
    lines.append("## Included Roles")
    lines.append("")
    for role in sorted(roles):
        lines.append(f"- [{role}]({role}/)")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    yaml = _load_yaml()

    parser = argparse.ArgumentParser(
        description="Generate Docusaurus docs for all giftpilz0 Ansible collections."
    )
    parser.add_argument(
        "--repo",
        default=HOMELAB_REPO,
        help=f"homelab repository URL to fetch (default: {HOMELAB_REPO}).",
    )
    parser.add_argument(
        "--repo-dir",
        default=None,
        help="Use a local checkout of the homelab repo instead of fetching.",
    )
    parser.add_argument(
        "--collections",
        default=None,
        help="Comma-separated list of collections to generate (default: all).",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Base output directory (default: <site>/docs/projects/ansible).",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    site_root = script_dir.parent
    out_base = Path(args.out).resolve() if args.out else site_root / SITE_ANSIBLE_DIR

    selected = set(args.collections.split(",")) if args.collections else None

    repo_root = fetch_homelab(args.repo, args.repo_dir)
    try:
        collections_root = repo_root / COLLECTIONS_REL
        if not collections_root.is_dir():
            raise SystemExit(f"No collections found under {collections_root}.")

        generated = 0
        for collection_dir in sorted(collections_root.iterdir()):
            if not collection_dir.is_dir():
                continue
            collection = collection_dir.name
            roles_dir = collection_dir / "roles"
            if selected is not None and collection not in selected:
                continue
            if not roles_dir.is_dir():
                continue

            galaxy: dict[str, Any] = {}
            galaxy_path = collection_dir / "galaxy.yml"
            if galaxy_path.is_file():
                with io.open(galaxy_path, encoding="utf-8") as fh:
                    galaxy = yaml.safe_load(fh) or {}
            description = (galaxy.get("description") or "").strip()
            if not description:
                description = f"Ansible collection: {collection}."

            role_specs: dict[str, dict[str, Any]] = {}
            for spec_path in sorted(roles_dir.glob("*/meta/argument_specs.yaml")):
                role = spec_path.parent.parent.name
                with io.open(spec_path, encoding="utf-8") as fh:
                    role_specs[role] = yaml.safe_load(fh) or {}

            if not role_specs:
                continue

            out_dir = out_base / collection
            out_dir.mkdir(parents=True, exist_ok=True)

            (out_dir / f"{collection}.md").write_text(
                render_collection_page(collection, description, list(role_specs)),
                encoding="utf-8",
            )

            for role in sorted(role_specs):
                # Load the role's defaults/main.yaml for non-container roles
                # whose argument specs do not carry defaults.
                defaults: dict[str, Any] = {}
                defaults_path = roles_dir / role / "defaults" / "main.yaml"
                if defaults_path.is_file():
                    with io.open(defaults_path, encoding="utf-8") as fh:
                        defaults = yaml.safe_load(fh) or {}

                (out_dir / f"{role}.md").write_text(
                    render_role_page(collection, role, role_specs[role], defaults),
                    encoding="utf-8",
                )

            generated += len(role_specs) + 1
            sys.stderr.write(f"  {collection}: {len(role_specs)} roles + index → {out_dir}\n")

        if generated == 0:
            raise SystemExit("No collections generated; nothing to do.")
    finally:
        if not args.repo_dir:
            shutil.rmtree(repo_root, ignore_errors=True)

    sys.stderr.write(f"Done. Generated {generated} pages.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
