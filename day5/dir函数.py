'''
模块说明：测试dir函数的使用
'''
import math

age = 12
name = 'tom'

def add(a,b):
    return a+b

# 系统函数dir()可以查看当前模块中包含的成员
print(dir())
print(__file__)
print(__name__)
print(__doc__)