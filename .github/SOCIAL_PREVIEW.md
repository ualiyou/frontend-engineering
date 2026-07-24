# Social Preview (Open Graph Image)

Specification for the repository's social preview — the 1280×640 image GitHub shows when the repo is shared on X, LinkedIn, Slack, Discord, etc. Set it under **Settings → Social preview**. This is a design spec, not an image; a designer or a script can produce the final PNG from it. A layout placeholder lives at [`../assets/branding/social-preview.svg`](../assets/branding/social-preview.svg).

## Canvas

- **Dimensions:** 1280 × 640 px (GitHub's 2:1 OG ratio). Export at 2× (2560 × 1280) then downscale for crispness.
- **Safe area:** keep all text within a 100 px margin; platforms crop edges unpredictably.
- **Format:** PNG (or JPG). Under 1 MB.

## Layout

A single, calm, left-aligned composition — not a collage.

```text
┌──────────────────────────────────────────────────────────┐
│  ▊ logo mark            Frontend Engineering               │  ← top-left lockup
│                                                            │
│     Engineering decisions, not tutorials.                  │  ← headline (tagline)
│                                                            │
│     A peer-reviewed knowledge base of patterns,            │  ← one-line subhead
│     trade-offs, and production-ready practices.            │
│                                                            │
│     ┌─ subtle node-graph motif, lower-right ─┐             │  ← graphic element
│  github.com/ualiyou/frontend-engineering  · MIT           │  ← footer meta
└──────────────────────────────────────────────────────────┘
```

## Typography

- **Wordmark / headline:** a geometric or grotesk sans — Inter, Geist, or IBM Plex Sans — Bold, ~72 px for the tagline.
- **Subhead:** the same family, Regular/Medium, ~34 px, 60–70% opacity.
- **Footer meta:** monospace (JetBrains Mono / Geist Mono), ~24 px, muted — echoes the "engineering" identity.
- Left-aligned, generous line-height (~1.25). No more than three type sizes total.

## Colors

A restrained, dark, "engineering" palette (matches the brand tokens in [`assets/branding`](../assets/branding)):

| Role | Hex | Use |
| --- | --- | --- |
| Background | `#0B1220` | Deep navy-black canvas |
| Surface accent | `#111a2e` | Subtle panel/vignette |
| Primary text | `#F5F7FA` | Headline, wordmark |
| Muted text | `#94A3B8` | Subhead, footer |
| Brand accent | `#38BDF8` | Logo mark, node-graph, one keyword highlight |
| Accent secondary | `#22D3AA` | Secondary graph nodes |

High contrast (primary text on background ≥ 12:1) so it stays legible as a small thumbnail.

## Graphic elements

- **Node-graph motif:** a light, low-opacity cluster of connected nodes in the lower-right — a direct nod to the knowledge map / dependency graph. Keep it subtle so text dominates.
- **Logo mark:** the `< >`-into-node monogram from the brand assets, in the brand accent.
- No stock photography, no gradients-of-the-week, no drop shadows. Flat, confident, technical.

## Branding rules

- Tagline text must match `PROJECT_IDENTITY.md` exactly.
- Never stretch or recolor the logo mark outside the accent palette.
- The image should read clearly at 320 × 160 (feed thumbnail) — verify by shrinking before shipping.
