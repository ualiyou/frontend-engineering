import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vitepress';
import { withMermaid } from 'vitepress-plugin-mermaid';
import { docsSidebar } from './sidebar.mts';

const REPO = 'https://github.com/ualiyou/frontend-engineering';

const config = withMermaid(
  defineConfig({
    // Project page: https://ualiyou.github.io/frontend-engineering/
    base: '/frontend-engineering/',
    lang: 'en-US',
    title: 'Frontend Engineering',
    description:
      'A peer-reviewed knowledge base of frontend engineering patterns, trade-offs, and production-ready practices — framework-aware, not framework-bound.',
    cleanUrls: true,
    lastUpdated: true,

    // The repo root is the content root, so articles keep their real paths and
    // every relative .md link between them works unchanged.
    srcExclude: [
      'node_modules/**',
      '.github/**',
      'templates/**',
      'profile-readme/**',
      'assets/**',
      // Generated matrices: useful in the repo, too large to publish as pages.
      'INTERNAL_LINKS.md',
      // The repo README is GitHub's landing page; index.md is the site's.
      'README.md',
    ],

    // The content uses GitHub's folder-index convention (`README.md`), and
    // articles link to their Part as a directory (`../`). Serving each README
    // as its folder's index makes both work without touching the markdown.
    rewrites: (id) => id.replace(/(^|\/)README\.md$/, '$1index.md'),

    // The learning paths deliberately link the full 651-article plan, most of
    // which is unwritten, so a site-level link gate here would only ever be
    // noise. Link integrity is enforced by lychee in `ci.yml` (which excludes
    // `paths/` and `templates/` for the same reason) and by
    // `scripts/validate-links.py` for the graph.
    ignoreDeadLinks: true,

    head: [
      // `.vitepress/public/` holds the site's static files: only paths under
      // it are served. logo.svg is a copy of assets/branding/logo.svg, and
      // favicon.ico is rendered from it (browsers request /favicon.ico
      // regardless of the declared icon).
      ['link', { rel: 'icon', type: 'image/svg+xml', href: '/frontend-engineering/logo.svg' }],
      ['link', { rel: 'alternate icon', type: 'image/x-icon', href: '/frontend-engineering/favicon.ico' }],
      ['link', { rel: 'apple-touch-icon', href: '/frontend-engineering/logo.svg' }],
      ['meta', { name: 'theme-color', content: '#38BDF8' }],
      ['meta', { property: 'og:type', content: 'website' }],
      ['meta', { property: 'og:title', content: 'Frontend Engineering' }],
      [
        'meta',
        {
          property: 'og:description',
          content: 'Engineering decisions, not tutorials.',
        },
      ],
      // Vazirmatn is the site's text face, in memory of Saber Rastikerdar.
      // One request for both families; preconnect because the font host is a
      // render-blocking third party on first paint.
      ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
      [
        'link',
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Vazirmatn:wght@100..900&display=swap',
        },
      ],
    ],

    themeConfig: {
      logo: '/logo.svg',
      siteTitle: 'Frontend Engineering',

      nav: [
        { text: 'Knowledge Map', link: '/KNOWLEDGE_MAP' },
        { text: 'Learning Paths', link: '/paths/' },
        {
          text: 'Reference',
          items: [
            { text: 'Article Inventory', link: '/ARTICLE_INVENTORY' },
            { text: 'Dependency Graph', link: '/GRAPH' },
            { text: 'Internal Linking Model', link: '/INTERNAL_LINKING' },
            { text: 'Anti-Patterns', link: '/anti-patterns/' },
            { text: 'Recipes', link: '/recipes/' },
            { text: 'Standards', link: '/standards/' },
          ],
        },
        {
          text: 'Project',
          items: [
            { text: 'Contributing', link: '/CONTRIBUTING' },
            { text: 'Governance', link: '/GOVERNANCE' },
            { text: 'Changelog', link: '/CHANGELOG' },
            { text: 'Support', link: '/SUPPORT' },
          ],
        },
      ],

      sidebar: {
        '/docs/': docsSidebar(),
      },

      outline: { level: [2, 3], label: 'On this page' },

      search: {
        provider: 'local',
        options: {
          detailedView: true,
        },
      },

      socialLinks: [{ icon: 'github', link: REPO }],

      editLink: {
        pattern: `${REPO}/edit/main/:path`,
        text: 'Edit this page on GitHub',
      },

      docFooter: { prev: 'Previous', next: 'Next' },

      footer: {
        message: `Peer-reviewed engineering decisions · <a href="${REPO}/blob/main/LICENSE">MIT licensed</a>`,
        copyright: 'Frontend Engineering',
      },
    },

    markdown: {
      lineNumbers: false,
      theme: { light: 'github-light', dark: 'github-dark' },
    },

    vite: {
      // srcDir is the repo root, so point Vite at the site's own static dir
      // instead of creating a top-level `public/` folder in a content repo.
      publicDir: fileURLToPath(new URL('./public', import.meta.url)),
    },

    mermaid: {
      theme: 'base',
      themeVariables: {
        fontFamily: 'Inter, system-ui, sans-serif',
        primaryColor: '#111a2e',
        primaryTextColor: '#F5F7FA',
        primaryBorderColor: '#38BDF8',
        lineColor: '#94A3B8',
        secondaryColor: '#0B1220',
        tertiaryColor: '#0B1220',
      },
    },
  }),
);

export default config;
