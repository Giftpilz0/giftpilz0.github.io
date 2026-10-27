import type { StarlightIcon } from "@astrojs/starlight/types";
import { categoryDirs, categoryLabel } from "./categories.ts";

export const topics: { label: string; link: string; icon: StarlightIcon; dir: string; unit: string }[] = [
  { label: "Documentation", link: "/docs/", icon: "open-book", dir: "docs", unit: "page" },
  { label: "Ansible Collections", link: "/projects/", icon: "puzzle", dir: "projects/ansible", unit: "role" },
];

/** Sidebar config for starlight-sidebar-topics: an overview link plus a group per category. */
export function sidebarTopics() {
  return topics.map(({ label, link, icon, dir }) => ({
    label,
    link,
    icon,
    items: [
      { label: "Overview", link },
      ...categoryDirs(dir)
        .map((directory) => ({
          label: categoryLabel(directory),
          collapsed: true,
          items: [{ autogenerate: { directory } }],
        }))
        .sort((a, b) => a.label.localeCompare(b.label)),
    ],
  }));
}
