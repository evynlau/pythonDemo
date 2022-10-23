# 定义字典tel，存储通讯录数据
tel = {"tom":8888,"jack":7777,"rose":6666}
print(len(tel))
print(tel['tom']) # 获取key为tom的元素的值
tel['tom'] = 7878 # 修改现有的key对象的value
print(tel)
# 遍历字典
for x in tel: # x是每个元素的key
    print(f'用户{x}的号码为{tel[x]}')
# 添加元素
tel['eric'] = 5555
print(tel)

# 获取所有的keys
print(tel.keys())

# items函数可以同时获取键和值
for (k,v) in tel.items():
    print(f'用户{k}的号码为{v}')