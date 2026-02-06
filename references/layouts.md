# Slide Layouts

Copy-paste HTML for each slide type.

---

## Title Slide

Opening slide. Centered. Sets the stage.

```html
<section class="slide slide--title">
    <p class="label">Category or Date</p>
    <h1>Main Title</h1>
    <p>Subtitle or tagline</p>
</section>
```

---

## Content Slide

Standard layout. Title + body + optional bullets.

```html
<section class="slide slide--content">
    <h2>Slide Title</h2>
    <p>Body text that explains the main point.</p>
    <ul>
        <li>Supporting point one</li>
        <li>Supporting point two</li>
        <li>Supporting point three</li>
    </ul>
</section>
```

---

## Bullets Slide

Large text bullets. For key takeaways.

```html
<section class="slide slide--bullets">
    <h2>Key Points</h2>
    <ul>
        <li>First major point</li>
        <li>Second major point</li>
        <li>Third major point</li>
        <li>Fourth major point</li>
    </ul>
</section>
```

---

## Split Slide

Text on one side, image on the other.

```html
<section class="slide slide--split">
    <div>
        <p class="label">Label</p>
        <h2>Title</h2>
        <p>Supporting text goes here.</p>
    </div>
    <div>
        <img src="image.png" alt="Description">
    </div>
</section>
```

---

## Quote Slide

Centered quotation with attribution.

```html
<section class="slide slide--quote">
    <blockquote>
        "The quote text goes here. Keep it memorable."
        <cite>— Person Name</cite>
    </blockquote>
</section>
```

---

## Image Slide

Full-bleed image. Optional caption.

```html
<section class="slide slide--image">
    <img src="hero.png" alt="Description">
    <figcaption>Optional caption</figcaption>
</section>
```

---

## Section Divider

Dark background. Signals a new section.

```html
<section class="slide slide--section">
    <p class="label">Part One</p>
    <h2>Section Title</h2>
</section>
```

---

## Code Slide

For showing code examples.

```html
<section class="slide slide--code">
    <h2>Code Example</h2>
    <pre><code>function example() {
    return "Hello, world";
}</code></pre>
</section>
```

---

## End Slide

Closing slide. Call to action.

```html
<section class="slide slide--end">
    <h2>Thank You</h2>
    <p>Questions? → email@example.com</p>
</section>
```

---

# Components

Use these inside any slide.

## Two Columns

```html
<div class="columns">
    <div>Left content</div>
    <div>Right content</div>
</div>
```

## Three Columns

```html
<div class="columns-3">
    <div>First</div>
    <div>Second</div>
    <div>Third</div>
</div>
```

## Card

```html
<div class="card">
    <h3>Card Title</h3>
    <p>Card description text.</p>
</div>
```

## Number Badge

```html
<span class="badge">1</span>
```

## Icon Row (Numbered Steps)

```html
<div class="icon-row">
    <span class="badge">1</span>
    <div>
        <h3>Step Title</h3>
        <p>Step description</p>
    </div>
</div>
```

## Label Text

```html
<p class="label">Category</p>
```

## Small Text

```html
<p class="small">Fine print or notes</p>
```

---

# Image Generation Prompts

Use these with nanobanana for consistent slide images.

## Hero/Background Images

```
"abstract gradient, [colors], minimal, professional, 16:9 aspect ratio"
```

Examples:
- `"abstract gradient, warm orange to deep purple, minimal, 16:9"`
- `"geometric pattern, navy blue and gold, corporate, 16:9"`
- `"soft gradient, pastel pink to light blue, calm, 16:9"`

## Concept Illustrations

```
"simple illustration of [concept], minimal line art, white background, professional"
```

## Data Visualization Style

```
"abstract representation of [concept], clean, modern, data visualization style, [color]"
```

## Photo-realistic

```
"professional photo of [subject], high quality, natural lighting, 16:9"
```
