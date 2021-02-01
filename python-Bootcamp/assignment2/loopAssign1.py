#Shreeji Patel
#105151171

sample_str = str(input('Please enter string: '))
index = len(sample_str)
revers_str = ''

while index>0:
    index-=1
    revers_str += sample_str[index]

print('Reversed string: %s' %revers_str)
