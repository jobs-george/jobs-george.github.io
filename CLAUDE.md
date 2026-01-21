# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Philosophy

This is a pure HTML-only personal website. **No CSS, no JavaScript.** The design prioritizes:
- Lightweight, fast loading
- Accessibility by default
- Semantic HTML structure
- Content over styling

## Site Structure

Three main HTML pages, all following the same structure:

- `index.html` - Homepage with about, latest work, and project archive
- `cv.html` - Curriculum vitae
- `publications.html` - Publications and dissertations

Each page shares:
- Consistent navigation header with links to all pages
- `<hr />` elements for visual separation between sections
- `id="top"` on `<body>` for "Back to top" footer links
- Favicon links (no web manifest)

## HTML Conventions

- **No CSS or JavaScript** - The site intentionally has zero styling or scripting
- **Semantic markup** - Use `<section>`, `<header>`, `<nav>`, `<footer>`, etc.
- **Visual separation** - Use `<hr />` tags between sections, not CSS
- **Navigation format** - Pipe-separated links: `<a href="...">LINK</a> | <a href="...">LINK</a>`
- **Consistent structure** - All pages follow the same pattern with double `<hr />` after header and before footer
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
