// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import { satteri } from "@astrojs/markdown-satteri";
import starlightLinksValidator from "starlight-links-validator";
import starlightSidebarTopics from "starlight-sidebar-topics";
import { sidebarTopics } from "./src/lib/topics.ts";
import { mermaidBlocks } from "./src/lib/mermaid.ts";

export default defineConfig({
  site: "https://giftpilz0.github.io",
  vite: {
    // Mermaid's diagram modules are large but only loaded on pages that use them.
    build: { chunkSizeWarningLimit: 1600 },
    // The package's ESM imports lack file extensions, which Node can't resolve; bundle it instead.
    environments: {
      prerender: { resolve: { noExternal: ["@material/material-color-utilities"] } },
    },
  },
  markdown: {
    processor: satteri({ mdastPlugins: [mermaidBlocks] }),
  },
  integrations: [
    starlight({
      title: "Nixpi",
      description: "Documentation about various tools",
      favicon: "/img/favicon.svg",
      logo: { src: "./src/assets/logo.svg" },
      social: [
        { icon: "github", label: "GitHub", href: "https://github.com/giftpilz0/giftpilz0.github.io" },
      ],
      editLink: { baseUrl: "https://github.com/giftpilz0/giftpilz0.github.io/edit/main/" },
      lastUpdated: true,
      disable404Route: true,
      customCss: [
        "@fontsource-variable/google-sans-flex",
        "@fontsource-variable/google-sans-code",
        "./src/styles/custom.css",
      ],
      components: {
        Head: "./src/components/Head.astro",
        ThemeSelect: "./src/components/ThemeSelect.astro",
      },
      expressiveCode: {
        styleOverrides: { borderRadius: "0.75rem" },
      },
      plugins: [
        starlightLinksValidator(),
        starlightSidebarTopics(sidebarTopics()),
      ],
    }),
  ],
});
