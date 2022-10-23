'''
根据蒙特,卡罗方法计算圆周率的近似值
'''
from random import random

def estimatePI(times):
    hits = 0 # 圆内部的随机点的数量
    for i in range(times):
        x = random()*2 - 1 # random可以获取0到1的随机小数
        y = random()*2 - 1
        if x*x + y*y <= 1:
            hits += 1
    return  4.0 * hits/times

print(estimatePI(10000))
print(estimatePI(100000))
print(estimatePI(1000000))
print(estimatePI(10000000))
print(estimatePI(100000000))