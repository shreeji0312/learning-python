#Shreeji Patel
#105151171

sample_str = str(input('Please enter a string: '))
flag = True
correct_str = ''

for i in range(len(sample_str)):
    if(sample_str[i] != ' '):
        correct_str += sample_str[i]
        flag = True 
    elif(sample_str[i] == ' '):
        if(flag):
            correct_str += sample_str[i] 
            flag = False
        else:
            pass

print('%s' %correct_str)