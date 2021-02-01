#Shreeji Patel
#105151171

print('Enter two points on a line: ')
X1 = int(input('X1:'))
X2 = int(input('X2:'))
Y1 = int(input('Y1:'))
Y2 = int(input('Y2:'))
print('Enter a point: ')
j = int(input('j: '))
k = int(input('k: '))
m = float((Y2-Y1)/(X2-X1))
b = float(Y1 - (m*X1))
if k == (m*j) + b:
    print('the point (%d, %d) is on the line y = %.0f*x + %.0f' %(j,k,m,b))
else:
    print('the point (%d, %d) is NOT on the line y = %.0f*x + %.0f' %(j,k,m,b))
