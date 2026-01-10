# pages-sample

This repo now contains three Sphinx projects.

Projects
--------

- `sites/landing`: landing site (root for Pages)
- `sites/site-a`: original site
- `sites/site-b`: second sample site

Build locally
-------------

```console
uv run make -C sites/landing html
uv run make -C sites/site-a html
uv run make -C sites/site-b html
```
