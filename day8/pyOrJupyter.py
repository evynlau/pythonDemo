import matplotlib.pyplot as plt # 可视化
import numpy as np
#%%
x1 = np.array([1,2,3,33,41,12,17,144,123,22,124,55])
y1 = np.array([7,234,5,67,88,222,2,12,31,44,55,6])
plt.scatter(x1,y1) #散点图
plt.show()
#%%
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title("散点图")
x1sort = sorted(x1)
y1sort = sorted(y1)
plt.plot(x1sort,y1sort,label='y1sort')  # 折线
plt.plot(x1sort,y1,c='g',label='y1',linestyle=':')
plt.scatter(x1sort,y1sort,marker='s',s=100,c='red') # 散点
plt.scatter(x1sort,y1,marker='*',s=100,c='b')
plt.xlabel('x轴',fontsize=18) # x轴标签
plt.ylabel('y轴',fontsize=12) # y轴标签
plt.legend() # 图例
plt.show()