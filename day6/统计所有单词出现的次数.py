'''
统计words.txt文档中，每一个单词出现的次数
并按照次数从大到小输出，输出内容为每个单词以及对应的次数
'''
f = open('files/words.txt','r',encoding='UTF-8')
content = f.read()
# 内容清洗
for c in content:
    if c in ('\n',',','\'','.','-','’'): # 判断是否为非法字符
        # 把字符串替换为空格
        content = content.replace(c,' ')
words = content.split(' ') #把字符串进行分割，得到列表words
# 统计每一个单词出现的次数
# ok,1
# hello,2
# python,2
# to,4
# .....
# [(ok,1),(hello,2),(python,2),(to,4)]
result = [] # 空列表，存储统计后的结果
s = set() # 定义一个集合{}
for w in words:  # 从列表中取出每一个单词
    if w in s:
        continue
    if w == '' or len(w) == 0:
        continue
    cnt = words.count(w) # 计算单词w出现的次数：cnt
    data = (w,cnt) # 得到一条数据
    result.append(data) # 将该条数据添加到列表
    s.add(w)  #把计算过的单词添加到集合中
# 排序
result.sort(reverse=True,key=lambda x:x[1])
print(result)
# 将结果保存到文件
f2 = open('files/words_count.txt','w',encoding='UTF-8')
f2.write('word count\n')
for data in result:
    # line = data[0] + " " + str(data[1]) + '\n' # 拼接一行字符串
    line = '%-15s %5d\n'%(data[0],data[1])
    f2.write(line)
f.close()
f2.close()

