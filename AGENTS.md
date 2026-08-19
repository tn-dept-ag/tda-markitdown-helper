# MarkItDown Helper Agent Notes

This repository contains a small internal tool for converting files to Markdown with MarkItDown.

## Scope

- Keep changes small and focused on the desktop app, Streamlit app, shared conversion logic, and launch scripts.
- Preserve the current two-option shape of the tool: Streamlit and desktop.
- Do not reintroduce a CLI unless the user explicitly asks for it.

## Working rules

- Prefer ASCII-only edits unless a file already uses non-ASCII text.
- Keep generated artifacts, virtual environments, caches, build outputs, and packaged binaries out of Git.
- Update `README.md` with a current `Last Updated` date when making significant changes.
- Validate Python edits with `py_compile` when possible.

## Verification

- For Python changes, run a syntax check or the narrowest practical smoke test.
- For Windows launchers, keep the commands simple and predictable for coworkers.

