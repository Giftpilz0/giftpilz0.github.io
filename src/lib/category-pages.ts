import { getCollection } from "astro:content";
import { categoryDirs, categoryLabel } from "./categories.ts";

export interface Category {
  label: string;
  href: string;
  pages: number;
}

/** Categories of a content directory, linking to their overview (`index`) or first page. */
export async function getCategories(dir: string): Promise<Category[]> {
  const entries = await getCollection("docs");
  return categoryDirs(dir)
    .map((directory) => {
      const pages = entries
        .filter(({ id }) => id.startsWith(`${directory}/`))
        .sort((a, b) => (a.data.sidebar.order ?? Infinity) - (b.data.sidebar.order ?? Infinity) || a.id.localeCompare(b.id));
      const overview = entries.find(({ id }) => id === directory);
      return {
        label: categoryLabel(directory),
        href: `/${(overview ?? pages[0]).id}/`,
        pages: pages.length,
      };
    })
    .sort((a, b) => a.label.localeCompare(b.label));
}
