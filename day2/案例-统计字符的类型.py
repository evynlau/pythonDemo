'''
输入一个字符串，统计字母、数字和空格的数量
'''
letter_num = 0
digit_num = 0
space_num = 0
other_num = 0
s = input('请输入一行字符串:')
for x in s:
    if x.isalpha():
        letter_num += 1
    elif x.isdigit():
        digit_num += 1
    elif x.isspace():
        space_num += 1
    else:
        other_num += 1
print(f'字母{letter_num}个，数字{digit_num}个，空格{space_num}个，其它字符{other_num}个')