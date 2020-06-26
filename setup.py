#! python3.8

from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
includefiles=['diapason.ico', 'assets\\' ]
setup(  name = "Diapason",
        version = "0.1",
        description = "Make a joyful noise!",
        author = "Bearheathen",
        options = {"build_exe": {'include_files':includefiles}},
        executables = [Executable("main.py", base=base, targetName="Diapason", shortcutName="Diapason", icon="diapason.ico")])
        