#Shreeji Patel
#105151171

num = int(input('Please enter any 3 digit num: '))
sum = num % 10
num /= 10
sum += int(num % 10)
num /= 10
sum += int(num % 10)
print('Sum: %d' %(sum))