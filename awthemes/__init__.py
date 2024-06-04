"""
A port of [tcl-awthemes] to Python ttk.
"""

import logging
from pathlib import Path
from tkinter import ttk

import tksvg  # type: ignore


log = logging.getLogger()


AWTHEMES_PATH: Path = Path(__file__).parent / "awthemes-10.4.0"


class AwthemesStyle(ttk.Style):
    """A style class that loads the awthemes themes into Tkinter."""
    awthemes_scalable: list[str] = [
        "awarc", "awblack", "awclearlooks", "awwinxpblue", "awbreeze",
        "awbreezedark", "awtemplate"
    ]
    awthemes: list[str] = ["awdark", "awlight"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tk.eval(f"set dir {AWTHEMES_PATH.as_posix()}")
        self.tk.eval(f"source {AWTHEMES_PATH.as_posix()}/pkgIndex.tcl")

    def theme_names(self) -> tuple[str]:
        return self.tk.splitlist(self.tk.call("ttk::themes"))

    def theme_use(self, themename: str | None = None) -> str | None:  # type: ignore[override]
        if themename is None:
            return super().theme_use(themename=None)
        is_tksvg_loaded = getattr(self.master, "_tksvg_loaded", False)
        if (themename in self.awthemes_scalable) and (not is_tksvg_loaded):
            tksvg.load(self.master)
        self.tk.call("package", "require", f"ttk::theme::{themename}")
        self.tk.call("ttk::setTheme", themename)
        return None
