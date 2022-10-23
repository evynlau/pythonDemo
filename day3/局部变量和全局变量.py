# a = 10  # 全局变量

def fun():
    b = 5  # 局部变量：函数内部定义的变量
    print(f'fun函数内部的变量b为{b}')
    global  a
    a = a + 1 # 无法修改
    print(f'在函数内访问变量a为{a}')
def fun2():
    b = 3
    print(f'fun2函数内部的变量b为{b}')
# print(b)
a = a + 1
print(a)
fun()