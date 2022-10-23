'''
随机生成10个整数，存入列表中，求10个数中的最大值，最小值
并按照从小到大的顺序输出
'''
import random
mylist = []  # 定义一个空列表
for n in range(1,11): # 构造一个执行10次的循环语句
    rand = random.randint(1,100)
    mylist.append(rand)  #将本次生成的随机数rand存入列表mylist中
list.sort(mylist) # 排序
for n in mylist:
    print(n,end=' ')
print()
print(f"最大值为{max(mylist)}，最小值为{min(mylist)}")