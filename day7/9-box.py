'''
定义box表示立方体类型，提供体积计算方法
'''
class box:
    def __init__(self,w,h,l):
        self.width = w
        self.height = h
        self.length = l
    def get_volumn(self):
        return self.width * self.height * self.length
# 创建对象
b1 = box(5,3,2)
b2 = box(6,2,3)
print(b1.get_volumn())
print(b2.get_volumn())