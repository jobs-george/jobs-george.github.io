# Website

Personal website for George, a research software engineer based in London. Built with semantic HTML and minimal CSS. No JavaScript. Hosted on GitHub Pages.

## Philosophy

This site prioritizes:
- Lightweight, fast loading
- Accessibility by default
- Semantic HTML structure
- Simple, clean styling with minimal CSS
- Automatic dark mode support

## Features

- **No JavaScript** - Pure HTML and CSS implementation
- **Semantic HTML5** - Proper use of `<article>`, `<section>`, `<time>`, and ARIA labels
- **Responsive design** - Mobile-friendly with viewport meta tags
- **Dark mode** - Automatic theme switching via CSS `@media (prefers-color-scheme: dark)`
- **Accessible links** - Descriptive link text throughout for screen readers
- **SEO optimized** - Includes sitemap.xml and robots.txt

## Structure

- `index.html` - Homepage with about, latest work, and project archive
- `cv.html` - Curriculum vitae
- `research.html` - Publications and dissertations
- `philosophy.html` - Website design philosophy
- `styles.css` - External stylesheet with minimal, clean styling and dark mode support
- `scripts/check_links.py` - Python script to validate external links in HTML files

## Getting Started

The website can be run locally by opening `index.html` in any web browser.

## Validation

External website links can be validated with the Python script:

```sh
# venv\Scripts\activate
python3 scripts/check_links.py
```

HTML can be validated at: https://validator.w3.org/

## Contribute

Feel free to open issues or submit pull requests if you spot any bugs or have suggestions for improvements!
