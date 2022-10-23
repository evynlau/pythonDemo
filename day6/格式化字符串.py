a = 1
b = 2
name ='jack'
# 占位符 %s 表示一个字符串变量
# 占位符 %d 表示一个整型变量
# 占位符 %f 表示一个浮点变量
print('hello,%s'% name)
print('%5d + %d = %d'%(a,b,a+b))
all = 567 # 总分
n = 15 # 人数
avg = all / n # 平均分
print('平均分是%.2f' % avg) # 控制小数点后的有效位数