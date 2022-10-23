'''
该模块实现数据的持久化操作，包含两个函数：文件的读取和文件的写入
'''
from  user import user

def read_file(path):
    with open(path,'r',encoding='UTF-8') as f:
        f.readline() #读取标题行
        book = [] # 定义一个空列表
        for line in f: # 自动循环读取f中的每一行数据
            # line表示一行数据，格式"tom tom@qq.com 19899990"
            words = line.split(' ')
            # 分割完成后做数据简单的处理
            # '19899990\n'
            # words[-1][-1] = '' # 去掉最后一个字符\n
            u = user(words[0],words[1],words[2][0:-1])
            book.append(u)
        return book

def write_file(book,path):
    '''
    将通讯录数据写入到文件中
    :param book: 通讯录数据，包含多个user对象的列表
    :param path: 文件的路径
    :return: 返回布尔类型，True表示写入成功，False表示写入失败
    '''
    with open(path,'w',encoding='UTF-8') as f:
        f.write('name email phone\n')
        for u in book:
            line = f'{u.name} {u.email} {u.phone}\n'
            f.write(line)