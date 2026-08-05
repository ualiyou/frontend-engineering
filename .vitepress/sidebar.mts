import fs from 'node:fs';
import path from 'node:path';

/**
 * Builds the docs sidebar from the repository itself, so the site can never
 * disagree with the content:
 *
 * - Parts come from the `docs/<nn-part>/` folders, labelled by their README H1.
 * - Domains come from each `graph.json` (`domain` field).
 * - Articles come from `graph.json` nodes, in `order`, filtered to the files
 *   that actually exist — planned articles are simply absent, never dead links.
 */

const DOCS_DIR = 'docs';

interface GraphNode {
  title: string;
  slug: string;
  order: number;
}

interface Graph {
  domain: string;
  nodes: GraphNode[];
}

export interface SidebarItem {
  text: string;
  link?: string;
  items?: SidebarItem[];
  collapsed?: boolean;
}

function firstHeading(file: string, fallback: string): string {
  try {
    const match = fs.readFileSync(file, 'utf8').match(/^#\s+(.+)$/m);
    return match ? match[1].trim() : fallback;
  } catch {
    return fallback;
  }
}

function titleCase(slug: string): string {
  return slug
    .split('-')
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

function directories(dir: string): string[] {
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .sort();
}

function domainItems(domainDir: string): SidebarItem[] {
  const graphPath = path.join(domainDir, 'graph.json');
  const present = new Set(
    fs
      .readdirSync(domainDir)
      .filter((name) => name.endsWith('.md') && name !== 'README.md'),
  );

  if (present.size === 0) return [];

  let nodes: GraphNode[] = [];
  if (fs.existsSync(graphPath)) {
    const graph = JSON.parse(fs.readFileSync(graphPath, 'utf8')) as Graph;
    nodes = [...graph.nodes].sort((a, b) => a.order - b.order);
  }

  const ordered = nodes
    .filter((node) => present.has(node.slug))
    .map((node) => ({
      text: node.title,
      link: `/${domainDir}/${node.slug.replace(/\.md$/, '')}`,
    }));

  // Anything on disk but missing from the graph still gets a link, so a new
  // article is never invisible just because graph.json wasn't updated yet.
  const linked = new Set(ordered.map((item) => item.link));
  const extras = [...present]
    .map((name) => ({
      text: titleCase(name.replace(/\.md$/, '')),
      link: `/${domainDir}/${name.replace(/\.md$/, '')}`,
    }))
    .filter((item) => !linked.has(item.link));

  return [...ordered, ...extras];
}

export function docsSidebar(): SidebarItem[] {
  const parts: SidebarItem[] = [];

  for (const part of directories(DOCS_DIR)) {
    const partDir = path.join(DOCS_DIR, part);
    const domains: SidebarItem[] = [];

    for (const domain of directories(partDir)) {
      const domainDir = path.join(partDir, domain);
      const items = domainItems(domainDir);
      if (items.length === 0) continue; // no published articles yet

      const graphPath = path.join(domainDir, 'graph.json');
      const label = fs.existsSync(graphPath)
        ? (JSON.parse(fs.readFileSync(graphPath, 'utf8')) as Graph).domain
        : firstHeading(path.join(domainDir, 'README.md'), titleCase(domain));

      domains.push({
        text: label,
        link: `/${domainDir}/README`,
        collapsed: false,
        items,
      });
    }

    if (domains.length === 0) continue;

    parts.push({
      text: firstHeading(path.join(partDir, 'README.md'), titleCase(part)),
      link: `/${partDir}/README`,
      collapsed: false,
      items: domains,
    });
  }

  return parts;
}
