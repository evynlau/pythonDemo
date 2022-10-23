
# 如果文件不存在，会自动创建指定目录的文件
# 如果文件存在，打开文件，清空内容
# 'w' 模式为写模式
# 'a' 模式为追加模式
f = open('咏鹅.txt','a',encoding='UTF-8')
f.write('鹅，鹅，鹅\n')
f.write('曲项向天歌\n')
f.write('白毛浮绿水\n')
f.write('红掌拨清波')

# 关闭文件
f.close()
