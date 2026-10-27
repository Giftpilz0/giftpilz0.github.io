#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = ["pyyaml"]
# ///
"""Generate the Ansible collection pages from the role argument specs in the homelab repo.

Each page stores its data in the frontmatter (schema in src/content.config.ts) and is
rendered by the components in src/components/ansible/.

Usage:

    # Fetch the latest homelab repo from GitHub:
    uv run scripts/generate_ansible_docs.py

    # Use a local checkout instead:
    uv run scripts/generate_ansible_docs.py --repo-dir /path/to/homelab

    # Only some collections, or a different output directory:
    uv run scripts/generate_ansible_docs.py --collections server,general --out /tmp/docs
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required. Install it with: pip install pyyaml")

HOMELAB_REPO = "https://github.com/Giftpilz0/homelab"
SITE_ANSIBLE_DIR = Path("src") / "content" / "docs" / "projects" / "ansible"
COMPONENTS_IMPORT = "../../../../../components/ansible"

def fetch_homelab(repo: str, repo_dir: str | None) -> Path:
    """Return the homelab checkout, shallow-cloning it into a temp dir unless given."""
    if repo_dir:
        path = Path(repo_dir)
        if not (path / "ansible_collections").is_dir():
            sys.exit(f"'{repo_dir}' has no ansible_collections directory; pass the homelab checkout root.")
        return path

    sys.stderr.write(f"Cloning {repo} ...\n")
    tmp = Path(tempfile.mkdtemp(prefix="generate_ansible_docs_"))
    subprocess.run(
        ["git", "clone", "--depth", "1", "--filter=blob:none", repo, str(tmp)],
        check=True,
        capture_output=True,
    )
    return tmp


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def sentence(text: str | list[str] | None) -> str | None:
    if isinstance(text, list):
        text = " ".join(text)
    text = " ".join((text or "").split())
    return text or None


def type_name(spec: dict[str, Any]) -> str:
    """Ansible's own type names, e.g. `str` or `list[dict]`."""
    name = spec.get("type", "str")
    return f"{name}[{spec['elements']}]" if spec.get("elements") else name


def format_default(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, str):
        return value if value else '""'
    if isinstance(value, (dict, list)):
        if not value:
            return "{}" if isinstance(value, dict) else "[]"
        return yaml.safe_dump(value, default_flow_style=False, sort_keys=False, allow_unicode=True).rstrip()
    return str(value)


def variable(name: str, spec: dict[str, Any], default: Any) -> dict[str, Any]:
    """One variable in the shape of `ansibleVariable` in src/content.config.ts."""
    var: dict[str, Any] = {"name": name, "type": type_name(spec)}
    if spec.get("required"):
        var["required"] = True
    if description := sentence(spec.get("description")):
        var["description"] = description
    if (formatted := format_default(spec.get("default", default))) is not None:
        var["default"] = formatted
    if spec.get("choices"):
        var["choices"] = [str(choice) for choice in spec["choices"]]
    if spec.get("options"):
        var["options"] = [variable(sub, sub_spec, None) for sub, sub_spec in spec["options"].items()]
    return var


def page(frontmatter: dict[str, Any], component: str) -> str:
    fm = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True, width=1000)
    return f"---\n{fm}---\n\nimport {component} from \"{COMPONENTS_IMPORT}/{component}.astro\";\n\n<{component} />\n"


def generate_collection(collection_dir: Path, out_dir: Path) -> int:
    """Write the overview and role pages of one collection; returns the number of roles."""
    galaxy = load_yaml(collection_dir / "galaxy.yml")
    collection = f"{galaxy['namespace']}.{galaxy['name']}"
    roles_dir = collection_dir / "roles"

    roles = []
    for spec_path in sorted(roles_dir.glob("*/meta/argument_specs.yaml")):
        role_dir = spec_path.parent.parent
        main = (load_yaml(spec_path) or {}).get("argument_specs", {}).get("main", {})
        defaults_path = role_dir / "defaults" / "main.yaml"
        defaults = (load_yaml(defaults_path) or {}) if defaults_path.is_file() else {}
        variables = [
            variable(name, spec, defaults.get(name)) for name, spec in (main.get("options") or {}).items()
        ]
        roles.append((role_dir.name, sentence(main.get("short_description")), variables))

    if not roles:
        return 0

    # Start from an empty directory so pages of deleted roles disappear.
    shutil.rmtree(out_dir, ignore_errors=True)
    out_dir.mkdir(parents=True)

    overview: dict[str, Any] = {"title": collection}
    if description := sentence(galaxy.get("description")):
        overview["description"] = description
    overview["sidebar"] = {"order": 0}
    overview["tableOfContents"] = False
    overview["ansibleCollection"] = {
        "name": collection,
        "roles": [
            {"name": name, "description": description, "variables": len(variables)}
            if description
            else {"name": name, "variables": len(variables)}
            for name, description, variables in roles
        ],
    }
    (out_dir / "index.mdx").write_text(page(overview, "AnsibleCollection"), encoding="utf-8")

    for name, description, variables in roles:
        frontmatter: dict[str, Any] = {"title": name}
        if description:
            frontmatter["description"] = description
        frontmatter["tableOfContents"] = False
        frontmatter["ansibleRole"] = {"collection": collection, "name": name, "variables": variables}
        (out_dir / f"{name}.mdx").write_text(page(frontmatter, "AnsibleRole"), encoding="utf-8")

    return len(roles)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", default=HOMELAB_REPO, help="homelab repository URL to clone.")
    parser.add_argument("--repo-dir", help="Use a local homelab checkout instead of cloning.")
    parser.add_argument("--collections", help="Comma-separated collections to generate (default: all).")
    parser.add_argument("--out", help=f"Output directory (default: {SITE_ANSIBLE_DIR}).")
    args = parser.parse_args()

    site_root = Path(__file__).resolve().parent.parent
    out_base = Path(args.out).resolve() if args.out else site_root / SITE_ANSIBLE_DIR
    selected = set(args.collections.split(",")) if args.collections else None

    repo_root = fetch_homelab(args.repo, args.repo_dir)
    try:
        total = 0
        for collection_dir in sorted((repo_root / "ansible_collections").glob("*/*/")):
            if not (collection_dir / "galaxy.yml").is_file():
                continue
            if selected is not None and collection_dir.name not in selected:
                continue
            count = generate_collection(collection_dir, out_base / collection_dir.name)
            sys.stderr.write(f"  {collection_dir.name}: {count} roles\n")
            total += count
        if total == 0:
            sys.exit("No roles found; nothing generated.")
    finally:
        if not args.repo_dir:
            shutil.rmtree(repo_root, ignore_errors=True)

    sys.stderr.write(f"Done. Generated {total} role pages.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
