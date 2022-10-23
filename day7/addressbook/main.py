from usercontrol import *
from file import  *

def print_menu():
    print('============通讯录============')
    print('1 显示通讯录')
    print('2 新增用户')
    print('3 删除用户')
    print('4 查找用户')
    print('0 退出')

def handle1(): # 1 显示通讯录
    showall_user()

def handle2(): # 2 新增用户
    name = input('请输入姓名:')
    email = input('请输入邮箱：')
    phone = input('请输入手机号：')
    if len(name) != 0 and len(email) != 0 and len(phone) != 0: # 验证非空
        u = user(name,email,phone) #  创建一个新的user对象
        f = add_user(u)
        if f:
            print('新增成功！')
        else:
            print('新增失败！已存在！')

def handle3(): # 3 删除用户
    phone = input('请输入要删除用户的手机号：')
    if len(phone) != 0:
        f = del_user(phone)
        if f:
            print('删除成功！')
        else:
            print('删除失败，手机号不存在！')
    else:
        print('手机号不能为空！')

def handle4(): # 4 查找用户
    name = input('请输入查找用户的姓名：')
    if len(name) != 0:
        u = search_user(name)
        if u == None:
            print('用户不存在！')
        else:
            print(u)
    else:
        print('用户名不能为空！')

# 程序运行时从文件初始数据.读取数据到book
# book = read_file('book.txt')  # 这种写法错误！！！
for u in read_file('book.txt'):
    book.append(u)

while True:
    print_menu() # 显示操作菜单
    while True:
        n = input('请输入一个合法的操作选项：')
        if n not in ('0','1','2','3','4'):
            continue
        else:
            break
    if n == '1':
        handle1()
    elif n == '2':
        handle2()
    elif n == '3':
        handle3()
    elif n == '4':
        handle4()
    else:
        break

# 程序退出前保存数据
write_file(book,'book.txt')