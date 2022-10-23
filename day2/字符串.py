'''
三引号：
这是一个多行注释符号
'''

s = '''
hi,
how are you
'''
print(s)
print('hello\nworld')
print('hello\tworld')
print("I\'m ok.")

# 判断合法的药名,全部由字母组成的药名是合法
names = ['abc','aabbcc','ad123','%$asdf']
for name in names:
    if name.isalpha(): # isalpha()函数的功能判断字符串是否全部由字母组成
        print(f'{name}是合法的')
    else:
        print(f'{name}不是合法的')