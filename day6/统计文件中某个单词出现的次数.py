'''
要求：读取文件words.txt,用户任意输入一个单词，统计该单词在文本中出现的次数
'''

# 读文件
f = open('files/words.txt','r',encoding='UTF-8')
# print(f) # f是文件对象
# 读取文件内容
content = f.read()
# print(content)
# 让用户输入要查找的单词
word = input('请输入你要查找的单词：')
# 统计字符串word在 content中出现的次数
# 方法1： 直接对整个字符串调用count方法，结果不准确
# cnt = content.count(word)
# print(f'单词{word}在文章中出现了{cnt}次。')
# 方法2 对初始的字符串进行分割，把分割出来的所有的单词存入列表中，对列表调用count
# 数据处理 ，字符串中所有的\n,,.-'等符号全部替换为空格
for c in content:
    if c in ('\n',',','\'','.','-','’'): # 判断是否为非法字符
        # 把字符串替换为空格
        content = content.replace(c,' ')
words = content.split(' ') # 用空格分割字符串，分割出来的单词放到一个列表中
print(words)
cnt = words.count(word);
print(f'单词{word}在文中出现了{cnt}次.')