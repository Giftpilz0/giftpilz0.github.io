import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

const config: Config = {
  title: "Nixpi",
  tagline: "Documentation about various tools",
  favicon: "img/favicon.svg",
  staticDirectories: ["static"],
  url: "https://giftpilz0.github.io",
  baseUrl: "/",

  // GitHub pages deployment
  organizationName: "giftpilz0",
  projectName: "giftpilz0.github.io",

  // warning
  onBrokenLinks: "warn",
  onBrokenAnchors: "warn",
  onBrokenMarkdownLinks: "warn",
  onDuplicateRoutes: "warn",

  // localization
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: "./sidebars.ts",
          editUrl:
            "https://github.com/giftpilz0/giftpilz0.github.io/tree/main/",
        },
        theme: {
          customCss: "./src/css/custom.css",
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // color
    colorMode: {
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },

    // sidebar
    docs: {
      sidebar: {
        hideable: true,
        autoCollapseCategories: true,
      },
    },

    // navbar
    navbar: {
      hideOnScroll: true,
      title: "Nixpi",
      logo: {
        alt: "Site Logo",
        src: "img/favicon.svg",
      },
      items: [
        {
          type: "docSidebar",
          sidebarId: "toolsSidebar",
          position: "left",
          label: "Documentation",
        },
        {
          type: "docSidebar",
          sidebarId: "projectSidebar",
          position: "left",
          label: "Projects",
        },
        {
          href: "https://github.com/Giftpilz0/giftpilz0.github.io",
          label: "GitHub",
          position: "right",
        },
      ],
    },

    // footer
    footer: {
      copyright: `Copyright © ${new Date().getFullYear()} Giftpilz0`,
    },


    // prism
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ["powershell", "bash", "json", "docker", "yaml"],
    },
  } satisfies Preset.ThemeConfig,

  // mermaid
  themes: ["@docusaurus/theme-mermaid"],
  markdown: {
    mermaid: true,
  },

  plugins: [require.resolve("docusaurus-lunr-search")],
};

export default config;
