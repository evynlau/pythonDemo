for letter in 'hello':
    print(letter,end=',')
# 统计一行字符串中出现了几个空格
msg = 'hello, how are you'
count = 0
for c in msg:
    if c == ' ':
        count += 1
print(f'字符串{msg}中含有{count}个空格。')
# 统计字符串的长度
# s = input('请输入一个字符串：')
# count = 0
# for x in s:
#     count = count + 1
# print(f'字符串{s}的长度为{count}')

# print(len(s))

# 使用for循环计算1到100的和
sum = 0
for x in range(1,101):
    sum = sum + x
print(f'1~100的和{sum}')

# for遍历列表
names = ["tom","tonny","jack","jenny","helen"]
for name in names:
    print(name)

