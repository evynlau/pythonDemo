'''
对于给定的数据源bill.txt：
1. 读取bill.txt文件的数据，完成数据清洗工作，要求去掉remarks值为"测试"的数据，
money字段的数据不是数字的记录删掉
2. 把清洗后的有效数据保存到备份文件bill.txt.bak
'''
file1 = open('bill.txt','r',encoding='UTF-8')
file2 = open('bill.txt.bak','w',encoding='UTF-8')
header = file1.readline()  # 读取bill.txt文件的第一行
file2.write(header) # 表头直接写入备份文件

for line in file1:   # for in可以自动遍历文件，按行获取内容
    # print(line)
    a = line.split(',') # 返回列表
    print(a)
    if a[4].strip() == "测试": # 过滤测试数据
        continue
    if not a[2].isdigit(): # 过滤金额格式不正确的数据
        continue
    # 合法的记录写入到备份文件中
    file2.write(line)
# 关闭文件
file1.close()
file2.close()


