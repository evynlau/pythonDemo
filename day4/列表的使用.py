# 定义列表，存储多个颜色值
colors = ['red','blue','purple','green']

# 访问某个颜色
print(colors[0])
print(colors[3])
# print(colors[6]) # colors 下标范围0～3 IndexError: list index out of range
# 使用反向索引访问元素
print(colors[-1])
print(colors[-3])
# print(colors[-8]) # IndexError
# 切片操作基本表达式：object[start_index : end_index : step]
# start_index 起始索引，包含
# end_index  结束索引，不包含
# step 步长，默认为1
numbers = [0,1,2,3,4,5,6,7,8,9,10]
print(numbers[1:5]) # 从下标为1的元素开始，到下标为5的元素前面
print(numbers[0::2]) # endindex没有定义，截取到最后
print(numbers[0:-5]) # 前闭后开
print(numbers[::])

# 运算符
print([1,2,3] + [3,4,5]) # 加法的功能是合并
print("hello " + "python")
print([1,2,3] * 3)
print(1 in [1,2,3]) # in运算符：成员运算符
print(5 in [1,2,3])
print(5 not in [1,2,3]) #not in 运算符

