#Shreeji Patel
#105151171

userinput = []
print('Enter number: ')

while True:
    num = int(input())
    if num == -1 : break
    
    #adding number to the list
    userinput.append(num)

userinput.sort()
topsix = userinput[-6:]

#Average 
average = sum(topsix) / len(topsix)
print('Average: %.14f' %average)

#median
mid = len(topsix) // 2
res = (topsix[mid] + topsix[~mid]) / 2
print("Median: %.1f" %res)