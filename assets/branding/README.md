# Brand Assets

Source and placeholder brand assets for Frontend Engineering. The SVGs here are **functional placeholders** — clean enough to ship today, meant to be replaced by final art.

| File | Purpose | Status |
| --- | --- | --- |
| `logo.svg` | Square mark (README hero, avatar) | Placeholder — usable |
| `banner.svg` | 1280×320 README banner | Placeholder — usable |
| `social-preview.svg` | 1280×640 Open Graph layout | Placeholder — export to `social-preview.png` for GitHub Settings → Social preview |

## Brand tokens

| Role | Hex |
| --- | --- |
| Background | `#0B1220` |
| Surface | `#111a2e` |
| Primary text | `#F5F7FA` |
| Muted text | `#94A3B8` |
| Accent (primary) | `#38BDF8` |
| Accent (secondary) | `#22D3AA` |

Typography: **Inter** (headings/body), **JetBrains Mono** (meta/code). The mark is a pair of code brackets `< >` around a small decision node-graph — the visual thesis of the project.

## Producing the PNG social preview

```bash
# with rsvg-convert (librsvg) or resvg / inkscape:
rsvg-convert -w 2560 -h 1280 social-preview.svg -o social-preview.png
```

See the full spec in [`../../.github/SOCIAL_PREVIEW.md`](../../.github/SOCIAL_PREVIEW.md).
