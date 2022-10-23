'''
学生成绩管理
将学生对象(包含姓名和成绩)存入列表中，并按成绩对学生进行排序,
并获取成绩最高和成绩最低的学生信息，
并将最高分和最低分的学生从列表删除，最后再对列表输出。
'''
# 如何表达/存储成绩单？
# s1 = {'name':'xiaohua','score':90}
# s2 = {'name':'xiaoming','score':98}
# sheet = [s1,s2]
# print(sheet[0]['score'])

# 面向对象思维模式
a = 12
b = "tom"
c = [1,2,3,4,5]
# 实现自定义类型，什么学生？
class student:
    # __init__ 特殊方法，内置方法，对象初始化方法，构造方法
    def __init__(self,n,s):# 参数n表示姓名，参数s表示成绩
        self.name = n # name属性赋值
        self.score = s # score属性赋值
    def study(self):
        print(f'{self.name}学生正在学习....')
    def print_stu(self):
        print(f'{self.name} {self.score}')

# 定义student类型的数据---创建student类型的对象
'''
s1 = student('xiaohua',90)  # 默认调用__init__方法，参数的签名必须一致
s2 = student('xiaohong',78)
s3 = student('xiaoming',99)
s4 = student('xiaoli',76)
s5 = student('xiaobing',85)
sheet = [s1,s2,s3,s4,s5]   # 一个班级的成绩单
print(sheet[0].score) # .是成员运算符
print(sheet[0].name)
'''
# 使用列表推导式随机创建20个学生的成绩
import random
sheet = [student(num,random.randint(1,100))
         for num in range(1001,1021)]
for s in sheet: # 遍历成绩单中的所有的学生
    s.print_stu() # 调用学生对象s的print_stu方法打印当前学生的信息
# 对成绩单进行排序，按照成绩从高到低
def sortbyscore(stu): # 定义排序规则，排序的关键字
    return stu.score
# sheet.sort(reverse=True,key=sortbyscore)
sheet.sort(reverse=True,key=lambda s:s.score)
print('排序后：')
for s in sheet:
    s.print_stu()

# 去掉最高分，最低分
del sheet[0]
del sheet[-1]

# 写入文件sheet.txt
with open('sheet.txt','w',encoding='UTF-8') as f:
    f.write('name score\n') #写入第一行，标题行
    for stu in sheet:
        line = str(stu.name) + ' ' + str(stu.score) + '\n' # newline
        f.write(line)


class product:
    # 如果类中没有定义构造方法，系统会提供一个默认__init__方法
    # 默认的__ini__是无参的
    # 当前类型没有属性
    # 如果定义了自己的构造方法，系统不提供
    def __init__(self,color,size):
        self.color = color
        self.size = size
    def show(self):
        print('我是一个产品。')
p1 = product('color','L')
print(p1.color)
print(p1.size)
# p1 = product()
# p1.color = 'red'
# p1.show()
# print(p1.color)

