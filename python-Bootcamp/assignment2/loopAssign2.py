#Shreeji Patel
#105151171

num = int(input('Please enter a num: '))
sum = 0

for i in range(1,num+1):
    sum += float(1/i)

print('the total is: %0.16f' %sum) 