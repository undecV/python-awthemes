# Python-Awthemes

This project is a port of the [tcl-awthemes] from Tcl/Tk to Python.
AWThemes is a library that provides attractive themes for Tcl/Tk,
and now these rich and appealing themes can be utilized in Python’s Tkinter applications.
This port allows Python developers to create GUI applications with a modern and appealing look more easily.

## Install

### Install from GitHub

```bash
pip install git+https://github.com/undecV/python-awthemes
```

alternatively, add this to your `requirements.txt` file:

```requirements.txt
python-awthemes @ git+https://github.com/undecV/python-awthemes.git@main
```

## Useage

```python
from awthemes import AwthemesStyle

root = tk.Tk()

# Load AwthemesStyle for your Tk root.
style = AwthemesStyle(root)

# Get all avaliable themes.
themes = style.theme_names()

# Set the theme.
style.theme_use("awdark")
```

## Development Remark

- [x] Tested for compatibility with `pygubu` and `pygubu-designer`.
- [x] Tested for compatibility with `pyinstaller` (with argumet `--collect-all "awthemes"`).
- [x] Tested for compatibility with `ttkwidgets`.

## Reference

- Tcler's Wiki: [awthemes](https://wiki.tcl-lang.org/page/awthemes)
- SourceForge: [tcl-awthemes][tcl-awthemes] (License: Zlib)
- GitHub: [ttkthemes](https://github.com/TkinterEP/ttkthemes) (License: GPL-3.0)
- PyPi: [types-ttkthemes](https://pypi.org/project/types-ttkthemes/) (License: Apache)
- PyPi: [ttkthemes2](https://pypi.org/project/ttkthemes2/) (License: MIT)

[tcl-awthemes]: https://sourceforge.net/projects/tcl-awthemes/
