#Shreeji Patel
#105151171

sample_str = str(input('Please enter string: '))
counti = 0
countj = 0
countk = 0
county = 1
length = len(sample_str)

for i in range(length+1):
    for j in range(length+1):
        if(i == 0 ):
            print(sample_str[counti], end = ' ')
            counti+=1
        elif(j ==0):
            print(sample_str[len(sample_str)-countk-1], end = ' ')
            countk+=1  
        elif(j == length):
            print(sample_str[county],  end = ' ')
            county+=1
            if(county == length):
                county = 0
        elif(i == length):
            print(sample_str[len(sample_str)-countj-1], end = ' ')
            countj+=1
        else:
            print(' ', end = ' ')
        if(counti == length or countj == length or countk ==length):
            counti = 0
            countj = 0
            countk = 0
    print()