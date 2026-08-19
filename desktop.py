from __future__ import annotations

import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

from converter import convert_path

try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
except ImportError:  # pragma: no cover
    TkinterDnD = None
    DND_FILES = None


class DesktopConverterApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("MarkItDown Helper")
        self.root.geometry("900x650")

        self.file_path: Path | None = None

        self._build_ui()
        self._configure_drag_drop()

    def _build_ui(self) -> None:
        outer = ttk.Frame(self.root, padding=16)
        outer.pack(fill="both", expand=True)

        title = ttk.Label(outer, text="MarkItDown Helper", font=("Segoe UI", 18, "bold"))
        title.pack(anchor="w")

        subtitle = ttk.Label(
            outer,
            text="Drop a file here or choose one, then convert it to Markdown.",
        )
        subtitle.pack(anchor="w", pady=(4, 12))

        controls = ttk.Frame(outer)
        controls.pack(fill="x", pady=(0, 12))

        ttk.Button(controls, text="Choose File", command=self.choose_file).pack(
            side="left"
        )
        ttk.Button(controls, text="Convert", command=self.convert_selected).pack(
            side="left", padx=(8, 0)
        )
        ttk.Button(controls, text="Save Markdown As...", command=self.save_markdown).pack(
            side="left", padx=(8, 0)
        )

        self.file_label = ttk.Label(outer, text="No file selected")
        self.file_label.pack(anchor="w")

        self.drop_zone = ttk.Label(
            outer,
            text="Drop a file here",
            anchor="center",
            relief="groove",
            padding=28,
        )
        self.drop_zone.pack(fill="x", pady=12)

        self.status = ttk.Label(outer, text="Ready")
        self.status.pack(anchor="w", pady=(0, 8))

        self.text = tk.Text(outer, wrap="word", undo=True, height=24)
        self.text.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(outer, command=self.text.yview)
        scrollbar.place(in_=self.text, relx=1.0, rely=0, relheight=1.0, anchor="ne")
        self.text.configure(yscrollcommand=scrollbar.set)

    def _configure_drag_drop(self) -> None:
        if TkinterDnD is None:
            self.drop_zone.configure(text="Drag and drop requires tkinterdnd2. Use Choose File.")
            return

        self.drop_zone.drop_target_register(DND_FILES)
        self.drop_zone.dnd_bind("<<Drop>>", self.on_drop)
        self.drop_zone.configure(text="Drop a file here")

    def choose_file(self) -> None:
        filename = filedialog.askopenfilename(
            title="Choose a file to convert",
            filetypes=[
                ("Supported files", "*.pdf *.docx *.pptx *.xlsx *.xls *.html *.htm *.csv *.txt *.md *.json *.jsonl *.epub *.zip"),
                ("All files", "*.*"),
            ],
        )
        if filename:
            self.set_file(Path(filename))

    def on_drop(self, event) -> None:  # noqa: ANN001
        dropped = self.root.tk.splitlist(event.data)
        if dropped:
            self.set_file(Path(dropped[0]))

    def set_file(self, path: Path) -> None:
        self.file_path = path
        self.file_label.configure(text=str(path))
        self.status.configure(text="File selected")

    def convert_selected(self) -> None:
        if not self.file_path:
            messagebox.showinfo("MarkItDown Helper", "Choose or drop a file first.")
            return

        self.status.configure(text="Converting...")
        self.root.update_idletasks()

        def worker() -> None:
            try:
                markdown = convert_path(self.file_path)
            except Exception as exc:  # noqa: BLE001
                self.root.after(0, lambda: self._show_error(exc))
                return
            self.root.after(0, lambda: self._show_markdown(markdown))

        threading.Thread(target=worker, daemon=True).start()

    def _show_error(self, exc: Exception) -> None:
        self.status.configure(text="Conversion failed")
        messagebox.showerror("Conversion failed", str(exc))

    def _show_markdown(self, markdown: str) -> None:
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", markdown)
        self.status.configure(text="Conversion complete")

    def save_markdown(self) -> None:
        content = self.text.get("1.0", tk.END).strip()
        if not content:
            messagebox.showinfo("MarkItDown Helper", "Nothing to save yet.")
            return

        default_name = "output.md"
        if self.file_path:
            default_name = f"{self.file_path.stem}.md"

        filename = filedialog.asksaveasfilename(
            title="Save Markdown",
            defaultextension=".md",
            initialfile=default_name,
            filetypes=[("Markdown", "*.md"), ("All files", "*.*")],
        )
        if not filename:
            return

        Path(filename).write_text(content, encoding="utf-8")
        self.status.configure(text=f"Saved {filename}")


def main() -> int:
    if TkinterDnD is not None:
        root = TkinterDnD.Tk()
    else:
        root = tk.Tk()

    DesktopConverterApp(root)
    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
