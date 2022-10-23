'''
整理药名：
医生在书写药品名的时候经常不注意大小写,格式比较混乱
现要求你写一个程序将医生书写混乱的药品名整理成统一规范的格式
即药品名的第一个字符如果是字母要大写,其他字母小写
如将ASPIRINASPIRIN、aspirinaspirin整理成AspirinAspirin
'''
# 定义一个列表存储多个药名
names = ["ASPIRINASPIRIN","aspirinaspirin","AspirinAspirin"]
# 循环遍历每一个药名
# for name in names:
#     name = name.capitalize()  # 名称规范操作，首字母大写，其它小写
i = 0
while i < len(names):
    names[i] = names[i].capitalize() # 第i个药名
    i = i + 1
print(names)