# 定义列表存储1～30之间能被3整除的数
multiples = []
for x in range(1,30):
    if x % 3 == 0:
        multiples.append(x)
print(multiples) # [3, 6, 9, 12, 15, 18, 21, 24, 27]
# 使用列表推导式来构造列表
# multiples = [i for i in range(1,30) if i%3 == 0]
multiples = [i for i in range(1,30)]
print(multiples)
# 定义一个列表 存储整数的平方
squares = [x**2 for x in range(10)]
print(squares)

a = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(a)

names = [' admin',' tom ','jack','tonny']
# new_names = []
# for name in names:
#     new_names.append(name.strip())
#strip函数可以去掉字符串两边的空格
new_names = [name.strip() for name in names]
print(names)
print(new_names)

names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
# 将姓名转为大写，过滤掉长度小于等于3的
new_names = [name.upper() for name in names if len(name)>3]
print(new_names) #['ALICE', 'JERRY', 'WENDY', 'SMITH']

dict = {x : x**2 for x in [1,2,3]}
print(dict)
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
dict = {name:len(name) for name in names}
print(dict)