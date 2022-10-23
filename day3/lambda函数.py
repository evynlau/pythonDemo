def my_sum(a,b):
    return a+b
# 使用lambda表达式定义一个匿名函数
my_sum = lambda x,y:x+y
print(my_sum(1,2))


users = ['tom','jack','rose','apple']
# 字符串排序按照字典序
users.sort() # 升序排列，reverse默认值为False，表示升序
users.sort(reverse=True) # 降序排列
# len是一个函数，把len函数作为参数传给sort函数
# key参数表示排序的依据和规范
users.sort(key=len,reverse=True)
print(users)

users = [('tom',12),('jack',15),('rose',10)]
# 按照用户的年龄降序排列
users.sort(reverse=True,key=lambda x:x[1])
print(users)
# 按照用户的姓名 升序排列
users.sort(key = lambda x:x[0])
print(users)

