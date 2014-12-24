import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup(	name="Gist Uploader",
		version='1.0',
		description="Uploads text to Gist",
		author="Roy Portas",
		executables= {Executable("gist_uploader.py", base=base)})