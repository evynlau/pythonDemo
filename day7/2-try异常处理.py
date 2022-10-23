try:
    a = int(input('a='))
    b = int(input('b='))
    print(a/b)
    print('b='+str(b))
except Exception as e:
    print(e)
print('end')