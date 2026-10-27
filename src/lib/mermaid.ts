import type { SatteriProcessorOptions } from "@astrojs/markdown-satteri";

type MdastPlugin = NonNullable<SatteriProcessorOptions["mdastPlugins"]>[number];

const escapeHtml = (text: string) =>
  text.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");

/** Turns ```mermaid code blocks into `<pre class="mermaid">` for MermaidRenderer.astro. */
export const mermaidBlocks: MdastPlugin = {
  name: "mermaid-blocks",
  code(node) {
    if (node.lang !== "mermaid") return;
    return { type: "html", value: `<pre class="mermaid">${escapeHtml(node.value)}</pre>` };
  },
};
