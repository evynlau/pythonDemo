from user import *

while True:
    print("欢迎进入**系统")
    print("1 注册 \n2 登录 \n3 修改密码  \n4 退出")
    choice = int(input("请选择操作类型："))
    match choice:
        case 1:
            name = input("请输入账号：")
            psd = input("请输入密码：")
            flag = register(name,psd)
            if flag == 3:
                print("注册成功！")
            elif flag == 1:
                print("注册失败！用户名不合法！")
            else:
                print("注册失败！用户名已存在！")
        case 2:
            name = input("请输入账号：")
            psd = input("请输入密码：")
            flag = login(name,psd)
            if flag:
                print('登录成功！')
            else:
                print('登录失败')
        case 3: # 修改密码
            name = input("请输入账号：")
            psd = input("请输入密码：")
            flag = login(name, psd) # 登录
            if flag: #登录成功
                new_psd = None
                while True:
                    new_psd = input("请输入新密码：")
                    if not is_valid_psd(new_psd):
                        print("密码不合法")
                    else:
                        break
                f = update_psd(name,new_psd) # 修改密码
                if f:
                    print("密码修改成功！")
                else:
                    print("密码修改失败！")
            else: # 登录失败
                print("登录失败！")
        case 4:
            print("系统退出！")
            break
        case _:
            print("请输入1～3之间的数字！")

