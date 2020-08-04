import sys
from  PyQt5.QtWidget import  QApplication,QWidget


if __name__ == '__main__':
    # Desiger.app  找到Desiger.app
    # 添加扩展工具  tools --> External Tools
    # 属性编辑器
    ui文件转化为py文件。
    方法一： 命令行。  python -m PyQt5.uic.pyuic deom.ui -o demo.py
    方法二：  pyuic5 demo.ui -o demo.py
    方法三： 扩展工具，
