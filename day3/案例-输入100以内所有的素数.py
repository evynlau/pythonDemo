import math
# 定义一个函数，判断一个数是否为素数
def isprime(a):
    if a <= 1: # 特殊情况先解决
        return  False
    i = 2
    m = math.sqrt(a)
    while i <= m:
        if a % i == 0:
            return False  # 函数中碰到return就函数体结束
        i = i + 1
    return True
# 主体代码
for i in range(1,101):
    # 判断当前i是否为素数
    if isprime(i):
        print(i,end=' ')

