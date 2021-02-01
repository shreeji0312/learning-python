#Shreeji Patel
#105151171


def subtract(a, b):
    c = a[:]
    for i in range(len(b)):
        if b[i] in c : c.remove(b[i])
    print(c)


'''
a = [1,2,3,4,5,6,7,8,9,10]
b = [2,5,6,7]
subtract(a,b)
'''