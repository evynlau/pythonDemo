# open 函数来打开一个指定文件
# open函数的参数说明
# 参数1： 文件的路径（绝对路径 或者 相对路径）
# 参数2： 文件操作类型：r：read，w：write，a：append
# open函数执行后返回文件对象
f = open("words.txt",'r',encoding='UTF-8')
# content = f.read() # 一次读取所有的内容
# print(content)
# print(f.read(10)) # 读取10个字符
print(f.readline()) # 每次读取一行
f.seek(0) # 将文件的指针重新指向文件头
print(f.readline()) # 每次读取一行
# 关闭文件
f.close()
