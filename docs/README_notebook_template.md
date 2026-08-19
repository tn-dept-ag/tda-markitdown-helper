# TDA Python Notebook Template

Suggested repository location:

```text
notebooks/tda_python_notebook_template.ipynb
```

## Purpose

This notebook is a reusable starting point for TDA GIS and Analytics Python workflows, especially ArcGIS Online / ArcGIS Enterprise automation, data QA/QC, hosted feature layer updates, and scheduled notebook jobs.

## Recommended commit steps

From the root of the `tda-template` repository, copy the notebook into `notebooks/` and commit it:

```bash
mkdir -p notebooks
cp /path/to/tda_python_notebook_template.ipynb notebooks/tda_python_notebook_template.ipynb
git add notebooks/tda_python_notebook_template.ipynb
git commit -m "Add standard TDA Python notebook template"
git push
```

If using the zip package, unzip it from the root of the repository and then run the `git add`, `git commit`, and `git push` commands above.

## Notes

- The notebook defaults to `update_mode = "dry_run"`.
- ArcGIS credentials are intentionally not stored in the notebook.
- The template includes placeholders for source loading, validation, transformation, export, hosted layer updates, item metadata, and run summaries.
- Local logs, outputs, cache folders, and sensitive data should be excluded from commits when appropriate.
