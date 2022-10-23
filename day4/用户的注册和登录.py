'''
案例需求：
1 定义列表users存储所有的用户，每一个用户信息包含账号和密码
2 提供注册功能，对用户输入的账号或者密码进行简单验证，注册成功，将新的用户信息
添加到users中
3 提供登录功能，提示用户输入账号和密码，判断用户是否存在，
存在则显示"登录成功！"，不存在显示"登录失败"
4 修改密码功能，首先用户登录成功，修改密码
'''
# 定义一个初始列表，默认提供一个管理员的账号
# users是一个列表，包含多个元素，每个元素是一个字典
users = [
    {'username':'admin','password':'123456'},
    {'username':'tom','password':'123'},
    {'username':'jack','password':'0000'}
]
# 定义函数，实现登录功能
def login(name,psd):
    # pass  # pass 空语句，不执行任何操作
    for user in users:
        # user是指的列表中的元素，类型字典
        if user['username'] == name and user['password'] == psd:
            return True
    # 循环执行完毕，所有的数据都进行比对，没发现相同的
    return False

# 定义函数，实现注册功能
def register(name,psd):
    if not is_valid_name(name):
        return 1  # 如果用户名不合法，注册失败

    # 判断账号是否存在
    for u in users:
        if u["username"] == name:
            return 2 # 注册失败，重名
    # 不存在就添加，注册成功
    user = {}
    user["username"] = name
    user["password"] = psd
    users.append(user) # 把新用户增加到列表中
    return 3  # 注册成功

# 定义函数，修改密码
def update_psd(name,new_psd):
    for u in users:
        if u["username"] == name:
            u["password"] = new_psd # 找到对应的用户，修改密码
            return True
    return False

# 定义函数，判断用户名是否合法，要求用户名只能包含字母，长度在6～20之间
def is_valid_name(name):
    if not name.isalpha():
        return False   # 不全由字母组成，用户名不合法
    if len(name) < 6 or len(name) > 20:
        return False
    return True # 用户名合法

#定义函数，判断密码是否合法，密码长度在6～20之间
def is_valid_psd(psd):
    psd_len = len(psd)
    if psd_len < 6 or psd_len > 20:
        return False
    else:
        return True

# 主程序
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


