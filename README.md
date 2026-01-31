# pages-sample

This repo now contains three Sphinx projects.

## Projects

- `sites/landing`: landing site (root for Pages)
- `sites/site-a`: original site
- `sites/site-b`: second sample site

## Build locally

```console
uv run make -C sites/landing html
uv run make -C sites/site-a html
uv run make -C sites/site-b html
```

## Autodoc example

Example `conf.py` fragment:

```python
extensions = [
    "sphinx.ext.autodoc",
]

import os
import sys

sys.path.insert(0, os.path.abspath("../../src"))
```

Example `docs/api.rst`:

```rst
API Reference
=============

.. automodule:: my_package
   :members:
   :undoc-members:
   :show-inheritance:
```
