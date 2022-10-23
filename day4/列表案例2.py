'''
去重和排序：
随机生成1～10之间的20个随机数，存入列表中
先输出原始的列表数据
对列表进行去重、排序后输出新列表
'''
import random
my_list = []
for n in range(20):
    rand = random.randint(1,10)
    my_list.append(rand) # append在末尾添加一个元素
#输出原始列表
for n in my_list:
    print(n,end=' ')
#去重
my_list2 = []
for n in my_list:
    if n not in my_list2: # 判断是否不存在
        my_list2.append(n)
print()
#输出去重并排序后的列表
list.sort(my_list2,reverse=True) # reverse 参数可以实现升序或者降序
for n in my_list2:
    print(n,end=' ')
