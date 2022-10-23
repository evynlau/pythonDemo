'''
定义类型表示分数，包含两个属性：分子和分母，提供分数常用的运算方法
'''
class fraction:
    # 魔法方法，对象初始化，也叫构造方法
    def __init__(self,top,bottom):
        self.top = top
        self.bottom = bottom
    # 魔法方法，对象描述的方法，可以返回一个字符串
    def __str__(self):
        return f'{self.top}/{self.bottom}'
    # 分数的加法
    def add(self,another):
        # self + another,两个都是分数对象，和存到self
        self.top = self.top * another.bottom + another.top*self.bottom
        self.bottom = self.bottom * another.bottom
    # 分数的加法
    def minus(self,another):
        # self - another,两个都是分数对象，差存到self
        self.top = self.top * another.bottom - another.top*self.bottom
        self.bottom = self.bottom * another.bottom
    def multiple(self,another):
        self.top = self.top * another.top
        self.bottom = self.bottom * another.bottom
    def divide(self,another):
        # self/another
        top = self.top * another.bottom
        bottom = self.bottom * another.top
        return fraction(top,bottom) # 完成计算后创建一个新的分数对象并返回

p1 = fraction(1,2)  # 自动调用__init__
print(p1)  # 自动调用__str__

p2 = fraction(1,3)
print(p2)

p1.add(p2) # 计算p1 + p2,结果存入p1
print(p1)

p1.multiple(p2) # 计算p1 * p2 结果存入p1
print(p1)

# 测试除法
f1 = fraction(1,4) # 被除数
f2 = fraction(1,3) # 除数
f3 = f1.divide(f2) # 商
print(f'{f1} 除以 {f2} 结果为 {f3}')
