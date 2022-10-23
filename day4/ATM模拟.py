'''
案例：模拟ATM机器功能
1 用户输入姓名，进入系统
2 显示操作菜单（1 查询余额  2 取款 3 存款 4 退出）
3 用户可以选择一项功能，完成之后再回到操作菜单
4 用户输入4 ，退出系统
'''
# 定义全局变量
money = 50000
name = None

def show_menu():
    print("1 查询余额")
    print("2 取款")
    print("3 存款")
    print("4 退出")
    return input("请输入您的操作：")

def query():
    print("-----查询余额------")
    print(f"{name},您好！您的余额为 {money}元。")

def saving(num): # num是函数的参数，形式参数
    global money
    money += num  # 使用glocal表示当前访问的money变量就是全局变量
    print(f"{name},您好！已成功存入 {num}元。")

# saving(1000) # 函数调用，1000传给num
# saving(2000) # 函数调用，2000传给num
def getmoney(num):
    global money
    money -= num
    print(f"{name},您好！已取款 {num}元。")
# getmoney(100)
# getmoney(500)

# 主程序
# 用户登录系统
name = input('欢迎使用ATM,请输入你的姓名：')

while True:
    choice = int(show_menu()) #获取数字 选项
    if choice == 1:
        query()
    elif choice == 2: #取款
        m = float(input('请输入取款金额：'))
        getmoney(m) # 实际参数，调用函数时，把m的值赋给num
    elif choice == 3:
        m = float(input('请输入存款金额：'))
        saving(m)
    elif choice == 4:
        print("88，欢迎下次使用！")
        break # 退出循环
    else:
        print(f"不存在选项{choice},请输入合法的选项！")












