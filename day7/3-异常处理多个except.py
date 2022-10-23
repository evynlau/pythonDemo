try:
    print('a')
    f = open('1.txt','r',encoding='UTF-8')
    # f = None
    # f.close()
except IOError as ie:
    print(ie)
except Exception as e:
    print(e)
else:
    print('success')
finally:
    print('finally')
    if f != None:
        f.close()
