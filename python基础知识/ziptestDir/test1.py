import platform  # 该模块用来访问平台相关属性。

os = platform.uname() # uname_result(system='Windows', node='SC-202006081647', release='10', version='10.0.18362', machine='AMD64', processor='Intel64 Family 6 Model 142 Stepping 10, GenuineIntel') <class 'platform.uname_result'>

print(os,type(os))
print(platform.node()) # SC-202006081647

print(platform.processor()) # Intel64 Family 6 Model 142 Stepping 10, GenuineIntel


import zipfile

# zipfile是python里用来做zip格式编码的压缩和解压缩的，由于是很常见的zip格式，

import zipfile
filename = " "
#z =zipfile.ZipFile(filename, 'r')
# 这里的第二个参数用r表示是读取zip文件，w是创建一个zip文件
# for f in z.namelist():
#     print(f)


def test1(name):
    ss  = f'xxxx{name}'
    return ss

if __name__ == "__main__":
    ss = 'name'
    s1 = test1(ss)
    print(s1)



