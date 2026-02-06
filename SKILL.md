---
name: accelr8-deck-builder
description: Create beautiful, shareable slide decks as webpages. Use when asked to make presentations, pitch decks, or slides. Generates images with nanobanana. Exports to PDF.
---

# ACCELR8 Deck Builder

Create slide decks as standalone HTML pages. Share as a link. Export as PDF. Generate images on demand.

## How It Works

1. Write the deck as a single HTML file
2. Generate images with nanobanana as needed
3. The webpage IS the deck — share the link
4. Export button downloads as PDF

## Creating a Deck

Every deck is a self-contained HTML file. Use the template in `references/template.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deck Title</title>
    <!-- Styles are embedded - no external dependencies -->
</head>
<body>
    <div class="deck" id="deck">
        <!-- Slides here -->
    </div>
    <div class="controls">
        <button onclick="exportPDF()">Export PDF</button>
        <button onclick="present()">Present</button>
    </div>
</body>
</html>
```

## Slide Layouts

See `references/layouts.md` for all available layouts:

- `slide--title` — Opening slide, centered
- `slide--content` — Standard content
- `slide--bullets` — Large bullet points
- `slide--split` — Text + image side by side
- `slide--quote` — Centered quotation
- `slide--image` — Full-bleed image
- `slide--section` — Dark section divider
- `slide--code` — Code examples
- `slide--end` — Closing slide

## Generating Images

When a slide needs an image, generate it with nanobanana:

```bash
uv run ~/.codex/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "abstract gradient, warm orange and deep purple, minimal, 16:9 aspect ratio" \
  --filename "slide-hero.png" \
  --resolution 2K
```

**Image workflow:**
1. Plan what images the deck needs
2. Generate each at 2K resolution (good balance of quality/speed)
3. Save to the deck folder
4. Reference with relative paths: `<img src="slide-hero.png">`

**Prompt tips for slides:**
- Include "16:9 aspect ratio" for full-bleed images
- Include "minimal, clean, professional" for business decks
- Include "abstract, gradient" for section backgrounds
- Be specific about mood: "warm", "corporate", "energetic", "calm"

## The Controls

Every deck includes:
- **Export PDF** — Downloads the deck as a PDF document
- **Present** — Fullscreen presentation mode (P key also works)
- **Arrow keys** — Navigate slides in presentation mode

## Sharing

The deck is a static HTML file. Share it by:
- Hosting on any static server (Vercel, Netlify, GitHub Pages)
- Sending the HTML file directly
- Dropping in a shared folder

## PDF Export

The export button uses the browser's print functionality with custom page sizing:
- Each slide becomes one PDF page
- 16:9 aspect ratio preserved
- High quality vector output

## Design Principles

1. **One idea per slide** — If you need more, make another slide
2. **Maximum 6 bullets** — Fewer is better
3. **Images for emotion** — Text for information
4. **Section dividers** — Every 3-4 slides for structure
5. **End with action** — What should they do next?

## File Structure

```
my-deck/
├── index.html      # The deck
├── hero.png        # Generated images
├── diagram.png
└── team-photo.png
```

## Quick Start

1. Copy `references/template.html` to your deck folder
2. Edit the slides
3. Generate images as needed with nanobanana
4. Open in browser to preview
5. Share the link or export PDF

---

*Build decks that move people.*
