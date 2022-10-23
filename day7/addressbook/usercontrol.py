'''
该模块实现user对象的管理操作，包括：查询、新增、删除、修改
'''
from user import user
book = []  # 通讯录对象，使用列表存储多个user对象
def add_user(u): #把用户对象u添加到book中
    # 判断用户是否已经存在，通过手机号判断
    for item in book:
        if item.phone == u.phone:
            return False
    book.append(u)
    return True

def showall_user(): # 显示通讯录中所有的信息
    for item in book:
        print(item)

def del_user(p): #p是被删除用户的手机号
    for item in book:
        if item.phone == p: # 当前的item就是要删除的用户
            book.remove(item)
            return True  # 删除第一个匹配的用户，则退出
    return False  # 手机号不存在

def search_user(name):
    for item in book:
        if item.name == name: # 按照姓名进行查找
            return item #返回查找到的用户
    return None  #没有找到返回空值
# 测试
if __name__ == '__main__':
    showall_user()  #打印刚开始的所有的用户信息
    add_user(user('helen','helen@qq.com','13745665656'))
    add_user(user('helen2', 'helen2@qq.com', '13745669999'))
    showall_user()