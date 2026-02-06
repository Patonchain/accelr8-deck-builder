# ACCELR8 Deck Builder

Create beautiful slide decks as webpages. Share as links. Export as PDF.

```
npx skills add Patonchain/accelr8-deck-builder
```

## Why

- PowerPoint is opaque to AI agents
- Webpages are shareable without software
- HTML + CSS = total design control
- Print to PDF when needed

## How It Works

```
Write HTML → Generate images → Share link → Export PDF
```

Each deck is a self-contained HTML file. Open in browser to present. Print to save as PDF. Host anywhere to share.

## Quick Start

1. Copy `references/template.html` to start a new deck
2. Edit the slides using layouts from `references/layouts.md`
3. Generate images with nanobanana as needed
4. Open in browser → Present or Export

## Features

- **9 slide layouts** — title, content, bullets, split, quote, image, section, code, end
- **Presentation mode** — Press P or click Present button
- **PDF export** — One click, properly formatted
- **Self-contained** — No dependencies, works offline
- **Dark theme** — Add `class="theme-dark"` to `<html>`

## Image Generation

Uses nanobanana (requires GEMINI_API_KEY):

```bash
uv run ~/.codex/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "abstract gradient, warm orange, minimal, 16:9" \
  --filename "hero.png" \
  --resolution 2K
```

## For AI Agents

See `SKILL.md` for complete instructions and `references/layouts.md` for all components.

## License

MIT
