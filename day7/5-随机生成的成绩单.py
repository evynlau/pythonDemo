'''
随机生成50个学生的三门功课成绩，学生的学号从1001～1050，求每个学生的总分和平均分,
按照总分降序排列，并把全部数据写入文件中
'''
import random

class student:
    def __init__(self,code,c,e,m):
        self.code = code
        self.chinese = c
        self.english = e
        self.math = m
        self.all = self.chinese+self.english+self.math
        self.avg = self.all/3
    def get_info(self):
        return '%s %d %d %d %d %.2f'%(self.code,self.chinese,self.english,self.math
                                      ,self.all,self.avg)
sheet = [student(str(num),random.randint(1,100),random.randint(1,100),random.randint(1,100))
         for num in range(1001,1051)]

# 按照总分从高到底排序
sheet.sort(reverse = True, key = lambda stu: stu.all)
# 写入文件
with open('sheet2.txt','w',encoding='UTF-8') as f:
    f.write('code chinese english math all average\n')
    for stu in sheet:
        line = stu.get_info() + '\n'
        f.write(line)
