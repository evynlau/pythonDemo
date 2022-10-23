name = "jack"
# len函数，求序列中元素的个数
print(len(name))

# 自定义一个函数，实现求一个容器中元素的个数
def my_len(s):
    cnt = 0 # 局部变量
    for x in s:
        cnt = cnt + 1
    return cnt

s = input('请输入一个字符串：')
print(my_len(s))