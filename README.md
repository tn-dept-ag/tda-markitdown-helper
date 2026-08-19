# MarkItDown Helper

This repo now has two ways to test the workflow:

- Streamlit web app for quick upload-and-copy use
- Desktop app with drag-and-drop support

## Install

```bash
cd C:\Users\be10cs1\github\tda-git\tda-markitdown-helper
python -m pip install -r requirements.txt
```

On Windows, you can use the included installer instead:

```bat
install_windows.bat
```

It creates a local `.venv` and installs the required packages.

## Streamlit web app

```bash
streamlit run app.py
```

Windows launcher:

```bat
run_web.bat
```

## Desktop app

```bash
python desktop.py
```

Drag-and-drop works when `tkinterdnd2` is available. If it is not installed or supported in your Python build, the app still works with the file picker.

Windows launcher:

```bat
run_desktop.bat
```

## Notes

- Both options use the same MarkItDown conversion path.
- The tool only processes local files you select or pass in.
