import zipfile

def unzip_file():
    r = zipfile.is_zipfile('./test.zip')  # 判断是不是  压缩文件
    if r:
        fz = zipfile.ZipFile('./test.zip', 'r') # 压缩文件列表

        for file in fz.namelist():
            print(file)
            fz.extract(file, './ziptestDir')
        print("*******")
    else:
        print('This is not zip')

def zip_file():
    zfile = zipfile.ZipFile("test.zip","w") # 创建一个对象
    zfile.write('test1.py')
    zfile.close()


if __name__== "__main__":
    zip_file()
    unzip_file()
