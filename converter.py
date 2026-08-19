from __future__ import annotations

import os
import tempfile
from pathlib import Path
from typing import Iterable

from markitdown import MarkItDown


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".pptx",
    ".xlsx",
    ".xls",
    ".html",
    ".htm",
    ".csv",
    ".txt",
    ".md",
    ".json",
    ".jsonl",
    ".epub",
    ".zip",
}


def is_supported_file(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS


def iter_supported_files(paths: Iterable[Path], recursive: bool = False) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file():
            if is_supported_file(path):
                files.append(path)
            continue

        if path.is_dir():
            pattern = "**/*" if recursive else "*"
            for candidate in sorted(path.glob(pattern)):
                if is_supported_file(candidate):
                    files.append(candidate)
    return files


def convert_path(path: Path, converter: MarkItDown | None = None) -> str:
    md = converter or MarkItDown()
    result = md.convert_local(str(path))
    return result.text_content or ""


def convert_bytes(filename: str, data: bytes, converter: MarkItDown | None = None) -> str:
    suffix = Path(filename).suffix or ".bin"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(data)
        tmp_path = Path(tmp.name)

    try:
        return convert_path(tmp_path, converter=converter)
    finally:
        try:
            os.unlink(tmp_path)
        except FileNotFoundError:
            pass

