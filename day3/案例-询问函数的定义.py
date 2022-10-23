def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# 位置参数方式进行调用
# ask_ok('are you sure to delete?',3,'try again')
# 关键字参数方式进行调用，可以不按照顺序传递
# ask_ok(prompt='do you want to quit?',reminder='invalid input,try again')
# ask_ok(prompt='do you want to quit?')

print('hello',end=',')

def userinfo(name,age,gender = 'male'):
    print(name,age,gender)

userinfo('admin',23) # 按照顺序传递，第三个参数不传取默认值
userinfo(age = 12,name='tom',gender='female') # 关键字传参数

# 定义不定长参数的函数，求多个整数的和
def addmoreint(*args):
    print(sum(args))
addmoreint(1,2,3)
addmoreint(4,55)
addmoreint(12,34,21)

def printinfo(**kargs):
    print(kargs)
printinfo(name='tom',age=12,gender='male')
printinfo(name='tom',age = 43)











