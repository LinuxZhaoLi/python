'''

lambda 是一个关键字
一个语法， 三个特性， 四个用法， 一个争论
一：语法唯一：
lambda argument_list: expression
二： 三个特性
    1 函数匿名
    2 有输入输出： 输入 是argument_list 输出是expression 结果
    3 功能简单
三： 四个用法
    1 将函数赋给变量
        add=lambda x,y;x+y
        add(1,3)
    2 将lambda函数赋值给其他函数，用lambda函数替换
        time.sleep=lambda x:None
    3 将lambda函数作为其他函数的返回值
        return lambda x,y:x+y
    4 将lambda函数作为参数传递给其他函数
        filter(lambda x:x%3==0,[1,2,3])
        sorted([1,2,3,4,5],key=lambda x:abs(5-x)
        map(lambda x: x+1,[1,2,3]) # 返回一个迭代器
        把一个函数作于array上
        reduce(lambda a,b:'{},{}'.format(a,b),[1,2,3,4,5,6])

'''
from functools import reduce  # 模块可以说主要是为函数式编程而设计，用于增强函数功能。
ss=sorted([1,2,3,4,5],key=lambda x:abs(5-x))
print(type(ss),ss)
mm = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(mm)
for i in mm:
    print(i)

rr = reduce(lambda a,b:'{},{}'.format(a,b),[1,2,3,4,5,6])
print(type(rr),rr)