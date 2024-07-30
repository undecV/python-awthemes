"""Test cases for AwthemesStyle."""

import logging
import os
import unittest
import tkinter as tk

from awthemes import AwthemesStyle


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()


class AwthemesStyleTest(unittest.TestCase):
    """Test cases for AwthemesStyle."""

    def setUp(self):
        if os.name != "nt" and os.getenv("GITHUB_ACTIONS"):
            os.system('Xvfb :1 -screen 0 1600x1200x16  &')
            os.environ["DISPLAY"] = ":1.0"


    def test_style_init(self) -> None:
        """Check whether style is init normally."""
        root = tk.Tk()
        style = AwthemesStyle(root)
        self.assertIsInstance(style.theme_names(), tuple)
        log.debug("Loaded themes: %r", style.theme_names())
        for theme in AwthemesStyle.awthemes + AwthemesStyle.awthemes_scalable:
            self.assertIn(theme, style.theme_names())

    def test_theme_use(self) -> None:
        """Check whether themes are set normally."""
        root = tk.Tk()
        style = AwthemesStyle(root)
        for theme in AwthemesStyle.awthemes + AwthemesStyle.awthemes_scalable:
            style.theme_use(theme)
            self.assertEqual(style.theme_use(), theme)

    def test_tksvg_loading(self) -> None:
        """Check whether TkSVG is loaded normally."""
        root = tk.Tk()
        self.assertFalse(bool(getattr(root, "_tksvg_loaded", False)))
        style = AwthemesStyle(root)
        for theme in AwthemesStyle.awthemes:
            style.theme_use(theme)
            self.assertFalse(bool(getattr(root, "_tksvg_loaded", False)))
        for theme in AwthemesStyle.awthemes_scalable:
            style.theme_use(theme)
            self.assertTrue(bool(getattr(root, "_tksvg_loaded", False)))
