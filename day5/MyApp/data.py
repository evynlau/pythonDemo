'''
该模块定义系统的数据
'''
# 定义一个初始列表，默认提供一个管理员的账号
# users是一个列表，包含多个元素，每个元素是一个字典
users = [
    {'username':'admin','password':'123456'},
    {'username':'tom','password':'123'},
    {'username':'jack','password':'0000'}
]
# __name__  内置的变量名，表示当前的模块名称
# 如果直接执行此模块，__name__的值__main__

# print("hello")

if __name__ == '__main__':
    print(__name__)
    print('hello')
    print(users[0]["username"])




