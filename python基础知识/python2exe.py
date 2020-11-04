from PyInstaller.__main__ import run

opts = ['xx.py','--clean','--win-private-assemblies', '-F']

run(opts)、

日志打印行号：
 __file__, sys.getframe().f_lineno
 