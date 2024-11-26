# Python-Awthemes

This project is a port of the [tcl-awthemes] from Tcl/Tk to Python.

Awthemes is a library designed for Tcl/Tk, featuring elegant themes such as ***light***, ***dark***, with ***scalable*** options. These stylish themes are now accessible for use in Python's Tkinter applications, making it easier for Python developers to design modern and visually engaging GUI applications.

## Glances

Check out Awthemes' screenshots and demos [here][TclersWiki-awthemes].

## Install

### Install from PyPI (Recommended)

[Python-Awthemes](https://pypi.org/project/python-awthemes/) is available in PyPI.

```bash
pip install python-awthemes
```

alternatively, add this to your `requirements.txt` file:

```requirements.txt
python-awthemes
```

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

- [x] Tested for compatibility with `pygubu` ([GitHub][alejandroautalan/pygubu]) and `pygubu-designer` ([GitHub][alejandroautalan/pygubu-designer]).
- [x] Tested for compatibility with `pyinstaller` ([Homepage](https://pyinstaller.org/)).
  - Add the argument `--collect-all "awthemes"` to your command.
  - If you're using scalable themes, include the argument `--collect-all "tksvg"` in the command as well.
- [x] Tested for compatibility with `ttkwidgets` ([PyPi](https://pypi.org/project/ttkwidgets/)).

[alejandroautalan/pygubu]: https://github.com/alejandroautalan/pygubu
[alejandroautalan/pygubu-designer]: https://github.com/alejandroautalan/pygubu-designer

## Reference

- Tcler's Wiki: [awthemes][TclersWiki-awthemes]
- SourceForge: [tcl-awthemes][tcl-awthemes] (License: Zlib)
- GitHub: [ttkthemes](https://github.com/TkinterEP/ttkthemes) (License: GPL-3.0)
- PyPi: [types-ttkthemes](https://pypi.org/project/types-ttkthemes/) (License: Apache)
- PyPi: [ttkthemes2](https://pypi.org/project/ttkthemes2/) (License: MIT)

[TclersWiki-awthemes]: https://wiki.tcl-lang.org/page/awthemes
[tcl-awthemes]: https://sourceforge.net/projects/tcl-awthemes/
