import shutil #shutil 模块提供了一系列对文件和文件集合的高阶操作

import shutil
f1 = open("file.txt","r")
f2 = open("file_copy.txt","a+")
shutil.copyfileobj(f1,f2,length=1024)