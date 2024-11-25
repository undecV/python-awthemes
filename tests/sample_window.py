#!python -m tests.sample_window
"""Sample window for testing."""


import logging
import tkinter as tk
from tkinter import ttk

import awthemes
from awthemes import AwthemesStyle


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


log.debug("Path of Python-Awthemes: %r", awthemes.__file__)


root = tk.Tk()

# Get all avaliable themes.
style = AwthemesStyle(root)
print(style.theme_names())
style.theme_use("awbreezedark")


root.title("TTK Sample Window")
root.geometry("400x300")

main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill="both", expand=True)

label = ttk.Label(main_frame, text="Welcome to TTK Sample Window!")
label.pack(pady=10)

entry = ttk.Entry(main_frame, width=30)
entry.pack(pady=10)

button = ttk.Button(
    main_frame, text="Click me.",
    command=lambda: label.config(text=f"The input is: {entry.get()}")
)
button.pack(pady=10)

options = ["Option 1", "Option 2", "Option 3"]
combo = ttk.Combobox(main_frame, values=options)
combo.set("Make a choice...")
combo.pack(pady=10)

root.mainloop()
