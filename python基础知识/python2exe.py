from PyInstaller.__main__ import run

opts = ['xx.py','--clean','--win-private-assemblies', '-F']

run(opts)