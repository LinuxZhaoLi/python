
from tkinter import *  #供了多个图形开发界面的库
from tkinter import ttk # 二者都有的组件，ttk将会覆盖Tkinter；ttk有而Tkinter没有的，将采用ttk的特性
root = Tk() # 创建一个窗口
if __name__=="__main__":
    root.title("视频现在工具")
    root.iconbitmap("./pic/title.ico")
    photo = PhotoImage(file = './pic/logo.png') #可以以GIF、PPM/PGM格式显示彩色图像的小部件。
    logo = Label(root,image=photo) # 创建一个label
    logo.pack() # 基类在每个小部件中使用方法包
    inputStart = Entry(root,bd=4,width=600) #允许显示简单文本的输入小部件
    labelStart=Label(root,text="请输入地址")
    labelStart.pack(anchor="w") # 排列方式
    inputStart.pack()
    labelQual = Label(root,text="请选择清晰度")
    labelQual.pack(anchor="w")
    inputQual = ttk.Combobox(root,state="readonly")
    inputQual["value"] = ('1080P','720P','480P','360P')
    keyTrans=dict() # 对应转化的字典
    keyTrans['1080P']='80'
    keyTrans['720P']='64'
    keyTrans['480P']='32'
    keyTrans['360']='16'
    inputQual.current(1) # 设置初始值
    inputQual.pack() # 排布\
    # 创建一个按钮， 并设置回调函数
    confirm = Button(root,text="开始下载",command=lambda:thread_it(do_prepare,inputStart.get(), keyTrans[inputQual.get()] ))
    root.mainloop() # 让窗口停留