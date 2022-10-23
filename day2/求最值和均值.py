'''
（求最值问题）依次读入10位学生的分数(0~100之间)，
计算并输出平均分（小数点后保留2位）、最高分和最低分。
平均分：求和功能，如何小数点后保留2位？
求最值：打擂台算法：假设第一个是最大的，和其它数依次比较，更大替换
'''
i = 0  # 循环变量
sum = 0 # 求和
score_min = 200 # 初始值
score_max = -1 # 初始值
while i < 10:
    score = float(input('请输入学生的成绩：'))  # 当前学生的成绩
    sum += score
    if score < score_min:  # 比较
        score_min = score   # 替换
    if score > score_max:
        score_max = score
    i = i + 1
# 此种写法无法控制小数点的有效位数
print(f'平均分为{sum/10.0},最高分{score_max},最低分{score_min}')
print('平均分为%.2f，最高分为%.2f，最低分为%.2f' % (sum/10,score_max,score_min))


