'''
此模块实现通讯录的数据持久化操作，包含文件的读取和写入
'''
def read_addr(file):
    f = open(file,'r',encoding='UTF-8')
    address = [] # 定义空列表
    f.readline() # 读表头
    for line in f: # 自动读取文件中的每一行
        # tom,tom@163.com,18898989999
        items = line.split(',')
        user = {
            'name':items[0],
            'email':items[1],
            'tel':items[2].strip()
        }
        address.append(user)
    return address # 完成文件读取后，返回通讯录列表

def write_addr(file,address):
    f = open(file,'w',encoding='UTF-8')
    f.write('name email tel\n') # 写入第一行
    for user in address:
        # tom,tom@163.com,18898989999
        line = f'{user["name"]},{user["email"]},{user["tel"]}\n'
        f.write(line)

if __name__ == '__main__':
    data = read_addr('addr.txt')
    print(data)
    # 新增一个用户
    data.append({'name':'jack','email':'jack@123.com','tel':13956567676})
    # 更新后的数据写入到文件中
    write_addr('addr.txt',data)