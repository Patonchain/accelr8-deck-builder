---
name: accelr8-deck-builder
description: Create beautiful slide decks as shareable webpages. Use when asked to make presentations, pitch decks, or slides. Exports to PDF. Generates images with nanobanana.
---

# ACCELR8 Deck Builder

Create slide decks as standalone HTML files. Share as a link. Export as PDF with one click.

## Quick Start

1. Create a new HTML file using the template below
2. Add slides using the layout classes
3. Generate images with nanobanana if needed
4. Open in browser to present or export

## Template

Every deck starts with this structure. Copy it exactly:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DECK TITLE HERE</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
</head>
<body>
    <div class="deck" id="deck">
        <!-- SLIDES GO HERE -->
    </div>
    <div class="controls">
        <button class="btn-secondary" onclick="present()">Present (P)</button>
        <button class="btn-primary" id="exportBtn" onclick="exportPDF()">Export PDF</button>
    </div>
    <div class="export-progress" id="exportProgress">
        <p id="exportStatus">Exporting slides...</p>
        <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
    </div>
</body>
</html>
```

The full template with all CSS and JS is in `references/template.html`. Copy that file to start a new deck.

## Slide Layouts

Each slide is a `<section class="slide slide--TYPE">`. Available types:

### Title Slide
```html
<section class="slide slide--title">
    <p class="label">Category</p>
    <h1>Main Title</h1>
    <p>Subtitle text</p>
</section>
```

### Content Slide
```html
<section class="slide slide--content">
    <h2>Slide Title</h2>
    <p>Body text here.</p>
    <ul>
        <li>Point one</li>
        <li>Point two</li>
        <li>Point three</li>
    </ul>
</section>
```

### Bullets Slide (Large)
```html
<section class="slide slide--bullets">
    <h2>Key Points</h2>
    <ul>
        <li>First major point</li>
        <li>Second major point</li>
        <li>Third major point</li>
    </ul>
</section>
```

### Split Slide (Text + Image)
```html
<section class="slide slide--split">
    <div>
        <p class="label">Label</p>
        <h2>Title</h2>
        <p>Description text.</p>
    </div>
    <div>
        <img src="image.png" alt="Description" crossorigin="anonymous">
    </div>
</section>
```

### Quote Slide
```html
<section class="slide slide--quote">
    <blockquote>
        "Quote text here."
        <cite>— Attribution</cite>
    </blockquote>
</section>
```

### Image Slide (Full Bleed)
```html
<section class="slide slide--image">
    <img src="hero.png" alt="Description" crossorigin="anonymous">
    <figcaption>Optional caption</figcaption>
</section>
```

### Section Divider
```html
<section class="slide slide--section">
    <p class="label">Part One</p>
    <h2>Section Title</h2>
</section>
```

### Code Slide
```html
<section class="slide slide--code">
    <h2>Example</h2>
    <pre><code>const x = 1;</code></pre>
</section>
```

### End Slide
```html
<section class="slide slide--end">
    <h2>Thank You</h2>
    <p>contact@example.com</p>
</section>
```

## Components

Use inside any slide:

```html
<!-- Two columns -->
<div class="columns">
    <div>Left</div>
    <div>Right</div>
</div>

<!-- Three columns -->
<div class="columns-3">
    <div>One</div>
    <div>Two</div>
    <div>Three</div>
</div>

<!-- Card -->
<div class="card">
    <h3>Title</h3>
    <p>Content</p>
</div>

<!-- Numbered step -->
<div class="icon-row">
    <span class="badge">1</span>
    <div>
        <h3>Step</h3>
        <p>Description</p>
    </div>
</div>
```

## Generating Images

Use nanobanana when slides need images:

```bash
uv run ~/.codex/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "abstract gradient, warm orange to purple, minimal, 16:9 aspect ratio" \
  --filename "hero.png" \
  --resolution 2K
```

**Prompt tips:**
- Always include "16:9 aspect ratio" for slide images
- Add "minimal, professional" for business decks
- Be specific: "warm", "corporate", "energetic", "calm"

## Features

- **Present button** — Fullscreen mode (or press P)
- **Export PDF** — Downloads PDF automatically, each slide = one page
- **Arrow keys** — Navigate in presentation mode
- **Escape** — Exit presentation

## Design Rules

1. One idea per slide
2. Maximum 6 bullet points
3. Images for emotion, text for information
4. Section dividers every 3-4 slides
5. End with clear call to action

## Sharing

The deck is a static HTML file. Share by:
- Hosting anywhere (Vercel, Netlify, GitHub Pages)
- Sending the file directly
- Dropping in shared folder

---

Read `references/template.html` for the complete working template with all styles and scripts.
