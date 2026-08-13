The pages are plain GitHub-flavoured Markdown so that they render correctly when
browsed here. Avoid MyST-specific directives (`:::{card}`, `:::{grid}`) — GitHub
shows them as raw text. GitHub alerts (`> [!NOTE]`) work in both places.

```
myst.yml            configuration and table of contents
README.md           repository landing page
doc/index.md        manual index
doc/ovl/            chapter: the OVL portal
doc/seascope/       chapter: the SEAScope application
doc/seashot/        chapter: the SEAShot tool
notebooks/          Jupyter examples, per tool
images/             logos and figures
```

To add a page, create the Markdown file in the relevant chapter directory under
`doc/`, link to it from that chapter's index, and add it to the `toc` in
`myst.yml`. Paths in the `toc` are relative to the repository root.

The same sources also build a [Jupyter Book 2](https://next.jupyterbook.org) site:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

jupyter book start          # live preview at http://localhost:3000
jupyter book build --html   # static site in _build/html
```

Pushing to `main` deploys that site to GitHub Pages via
`.github/workflows/deploy.yml`, which requires *Settings → Pages → Source* to be
set to **GitHub Actions**.