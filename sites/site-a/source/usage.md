# Usage Guide

This page shows a few more structures that are handy for documentation.

## Pages and navigation

Each page is a `.md` file stored under `source/`. Add the filename (no
extension) to the root `toctree` so it appears in the sidebar.

## Build tasks

| Task | Command |
| --- | --- |
| Build HTML | `make html` |
| Clean output | `make clean` |

## Include snippets

Use `literalinclude` when you want to embed code from a file.

```rst
.. literalinclude:: ../Makefile
   :language: make
```
