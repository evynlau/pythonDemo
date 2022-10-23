'''
要求：读取文件words.txt,用户任意输入一个单词，统计该单词在文本中出现的次数
'''
# 读文件
f = open('files/words.txt','r',encoding='UTF-8')
# print(f)
# 读取文件所有的内容，得到一个字符串content
content = f.read()
# 内容清洗
for c in content:
    if c in ('\n',',','\'','.','-','’'): # 判断是否为非法字符
        # 把字符串替换为空格
        content = content.replace(c,' ')
words = content.split(' ') # 用空格分割字符串，分割出来的单词放到一个列表中

# 让用户输入要查找的单词
word = input('请输入你要查找的单词：')
cnt = words.count(word);

print(f'单词{word}在文中出现了{cnt}次.')