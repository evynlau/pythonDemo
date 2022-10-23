# 函数定义（没有参数）：实现简单的打招呼功能
def sayHello():
    print('hello')

# 函数定义（包含一个参数）：实现向谁打招呼的功能
def sayHelloTo(name):  # name是形参
    print(f'hi,{name}')
# 函数定义（包含两个参数）
def login(name,pwd):
    if name == 'admin' and pwd == '123':
        return  True
    else:
        return  False

def add(a,b):
    c = a + b
    return  c

# 调用函数
login('tom','123')
# login('123','tom')
# sayHello()
# sayHello()
# sayHelloTo('tom')  # 'tom'为函数实参
# sayHelloTo('rose')
while True:
    name = input('name:')
    pwd = input('password:')
    f = login(name,pwd)  # 调用函数判断登录结果
    if f:
        print(f'welcome {name}!')
        break
    else:
        print('error! please input again!')




