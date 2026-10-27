import { existsSync, readdirSync, readFileSync } from "node:fs";

const CONTENT_DIR = "src/content/docs";

/** Sub-directories of a content directory, e.g. `docs/git` for `docs`. */
export function categoryDirs(dir: string): string[] {
  return readdirSync(`${CONTENT_DIR}/${dir}`, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => `${dir}/${entry.name}`);
}

/** The `label` from the folder's `_category_.json`, else the folder name. */
export function categoryLabel(directory: string): string {
  const meta = `${CONTENT_DIR}/${directory}/_category_.json`;
  return existsSync(meta)
    ? JSON.parse(readFileSync(meta, "utf-8")).label
    : directory.slice(directory.lastIndexOf("/") + 1);
}
