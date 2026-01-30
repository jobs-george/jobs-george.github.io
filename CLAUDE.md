# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Philosophy

This is a minimal personal website built with semantic HTML and basic CSS. **No JavaScript.** The design prioritizes:
- Lightweight, fast loading
- Accessibility by default
- Semantic HTML structure
- Simple, clean styling with external CSS

## Site Structure

Three main HTML pages, all following the same structure:

- `index.html` - Homepage with about, latest work, and project archive
- `cv.html` - Curriculum vitae
- `research.html` - Publications and dissertations
- `philosophy.html` - Website design philosophy

**Styling:**
- `styles.css` - External stylesheet with minimal, clean styling (monospace fonts, centered layout, subtle borders)

Each page shares:
- Link to external `styles.css` stylesheet
- Consistent navigation header with links to all pages
- `<hr />` elements for visual separation between sections
- `id="top"` on `<body>` for "Back to top" footer links
- Favicon links (no web manifest)

## HTML Conventions

- **External CSS, no JavaScript** - Basic styling via `styles.css`, no scripting
- **Minimal CSS** - Styling focuses on typography, spacing, and layout (monospace font, centered content, subtle section borders)
- **Semantic markup** - Use `<section>`, `<header>`, `<nav>`, `<footer>`, etc.
- **Visual separation** - Use `<hr />` tags between major sections
- **Navigation format** - Pipe-separated links: `<a href="...">LINK</a> | <a href="...">LINK</a>`
- **Consistent structure** - All pages follow the same pattern with `<hr />` after header and before footer
- **Back to top links** - Footer includes `<a href="#top">Back to top ↑</a>`

## Validation & Testing

Validate external links using the Python script:

```sh
python3 app.py
```

This script (using BeautifulSoup and requests) checks all external HTTPS links in `index.html` and `cv.html` to ensure they return 200 status codes.

Validate HTML at: https://validator.w3.org/

## SEO Files

- `sitemap.xml` - Keep updated with all HTML pages, use current date for `<lastmod>`
- `robots.txt` - Allows all crawlers
- No web manifest (archived for simplicity)

## Archive Folder

`.archive/` contains previous versions and assets that are no longer used:
- Original HTML files with CSS frameworks
- `site.webmanifest` (removed for simplicity)
- Other deprecated assets

Do not reference or restore files from `.archive/` unless explicitly requested.
