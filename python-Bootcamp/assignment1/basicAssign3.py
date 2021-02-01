#Shreeji Patel
#105151171

import random

comp = int(input('Please enter Ur guess between 1 to 9: '))
rand = random.randint(1,9)
if comp==rand:
    print('Correct')
else:
    print('Incorrect. The correct number was %d' %(rand))