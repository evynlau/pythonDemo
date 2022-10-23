'''
user模块：定义和用户相关的操作，包括登录、注册、修改密码等；
'''
# import data
from data import users

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

if __name__ == '__main__':
    f = login('admin', '123456')
    print(f)