# MarkItDown Helper

This repo now has two ways to test the workflow:

- Streamlit web app for quick upload-and-copy use
- Desktop app with drag-and-drop support

## Install

For the easiest coworker path, download the Windows EXE from the GitHub release:

- [MarkItDown Helper v0.1.0](https://github.com/tn-dept-ag/tda-markitdown-helper/releases/tag/v0.1.0)

If you are running the repo locally:

```bash
cd C:\Users\be10cs1\github\tda-git\tda-markitdown-helper
python -m pip install -r requirements.txt
```

On Windows, you can use the included installer instead:

```bat
install_windows.bat
```

It creates a local `.venv` and installs the required packages.

For coworkers, the simplest starting point is `launch.bat`, which lets them choose between the desktop app and the Streamlit app from one menu.

## Streamlit web app

```bash
streamlit run app.py
```

Windows launcher:

```bat
launch.bat
```

Direct launcher:

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
launch.bat
```

Direct launcher:

```bat
run_desktop.bat
```

## Package a Desktop EXE

```bat
build_desktop_exe.bat
```

This produces `dist\MarkItDownHelper.exe` for coworkers who prefer a double-clickable desktop app instead of launching Python directly.

## Notes

- Both options use the same MarkItDown conversion path.
- The tool only processes local files you select or pass in.

Last Updated: 2026-08-19
