'''
斐波那契数列：
1 1 2 3 5 8 13 ......
'''
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2) # 函数体中有自用自身的代码
# f(50)->f(49)-f(48)....f(1)
print(fib(3))
print(fib(10))
# 输入数列中的前20个，使用空格隔开
for i in range(1,51):
    print(fib(i),end=' ')
