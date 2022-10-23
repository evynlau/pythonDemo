'''
user模块：定义user类型
'''
class user:
    def __init__(self,n,e,p):
        self.name = n
        self.email = e
        self.phone = p
    def __str__(self):
        return f'{self.name} {self.email} {self.phone}'

if __name__ == '__main__':
    tom = user('tom','tom@qq.com','18898989999')
    print(tom)