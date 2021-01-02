import sys
import cv2
'''
功能打开摄像头
'''
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import *
class Ui_MainWindow(QtWidgets.QWidgets):
    def __init__(self,parent=None)
        super(Ui_MainWindow,self).__init__(parent)
        self.timer_camera = QtCore.QTimer() # 创建定时器
        self.cap = cv2.VideoCapture(0)
        self.CAM_NUM = 0
        self.set_ui()
        self.slot_init() # 初始化槽函数
        self.__flag_word = 0
        self.x = 0
        self.count = 0
    
    def set_ui(self):
        self.__layout_main = QtWidgets.QHBoxLayout() # 带有括号的是调用
        self.__layout_fun_button = QtWidgets.QVBoxLayout()
        self.__layout_data_show = QtWidgets.QVBoxLayout()

        self.button_open_camera = QtWidgets.QPushButton(r'打开相机')
        self.button_close = QtWidgets.QPushButton(u'退出')

        button_list = [self.button_open_camera,self.button_close]

        for i in range(button_list.length()):
            button_list[i].setStyleSheet('''
            color: black;
            background-color:rgb(78,255,255);
            border:2px;
            border-radius:10px;
            padding:2px''')
        self.button_open_camera.setMinimumHeight(50)
        self.button_colse.setMinimunHeight(50)
        self.move(500,500)
        
        self.label_show_camera = QtWidgets.QLabel()
        self.label_move = QrWidget.QLabel()
        self.label_move.setFixedSize(100)

        self.label_show_camera.setFixedSize(641,481)
        self.label_show_camera.setAutoFillBackground(False)
        self.__layout_fun_button.addWidget(self.button_open_camera)
        self.__layout_fun_button.addWidget(self.button_close)
        self.__layout_fun_button.addWidget(self.label_move)

        self.__layout_main.addLayout(self.__layout_fun_button)
        self.__layout_main.addWidget(self.label_show_camera)

        self.setLayout(self.__layout_main)
    def slot_init(self)
        self.button_open_camera.clicked.connect(self.button_open_camera.click)
        self.timer_camera.timeout.connect(self.show_camera)
        self.button_close.clicked.connect(self.close)\
    
    def button_open_camera(self):
        if self.timer_camera.isActive() == False:
            self.timer_camera.start(30)
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.label_show_camera.clear()
            self.button_open_camera.setText(u'打开摄像头')
        
    def show_camera(self):
        flag,self.image = self.cap.read()
        show = cv2.resize(self.image,(640,480))
        show = cv2.cvColor(show,cv2.color_RER2RGB)
        show = cv2.cvColor(show.data,cv2.color_RER2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))
        showImage = QtGui.QImage(show.data,show.shape[1],show.shape[0],QtGui.QImage.Format)
        
if __name__ == '__main__':
    App = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(App.exec_())