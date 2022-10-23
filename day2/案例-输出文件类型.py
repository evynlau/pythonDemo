'''
输入一个图片的名称，输出文件类型
（使用rfind方法从右向左进行特定字符的查找）
'''
filenname = input('输入一张图片的名称：') # icon.png
#rfind()函数从右向做查找第一个符合的子串，返回下标
point_index = filenname.rfind('.')
# 截取子串，从字符.的下一个位置开始，直到最后
print(filenname[point_index+1:])
