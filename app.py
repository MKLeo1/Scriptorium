#!/usr/bin/env python3

import os
import sys

"""Replace the virtual environment path with your own or install the Custom Tkinter package on your system"""

# venv path
venv_python = "/home/leo/VirtualEnvironments/python3customtkinter_env/bin/python3"

if sys.executable != venv_python:
    os.execv(venv_python, [venv_python] + sys.argv)

from components.main_app_window import MainAppWindow

if __name__ == "__main__":
    app = MainAppWindow()
    app.mainloop()
