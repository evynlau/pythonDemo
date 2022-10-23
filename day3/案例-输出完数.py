'''
一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
'''
def isperfect(a):
    s = 0
    for i in range(1,a):
        if a % i == 0: # i是a的一个因子
            s += i
    if s == a:
        return True
    else:
        return False

for i in range(1,1001):
    if isperfect(i):
        print(i)

