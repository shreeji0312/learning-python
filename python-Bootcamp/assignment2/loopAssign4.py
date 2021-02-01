#Shreeji Patel
#105151171

print("Enter a number. enter 0 to exit.")

count = 0
sum = 0.0
number = int(input(""))
small = number
largest = number

while number != 0:
    if(small > number):
        small = number
    if(largest < number):
        largest = number
    sum += number
    count+=1
    number = int(input(""))

print('Average: %.2f \nLargest: %d \nSmallest: %d' %(sum/count, largest, small))