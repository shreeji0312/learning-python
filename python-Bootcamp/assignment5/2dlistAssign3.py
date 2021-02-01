#Shreeji Patel
#105151171

import random
import math

def check(area, x1, y1):
    for x2 in range(30):
        for y2 in range(30):
            if area[x2][y2] == 'x':
                d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                if d<3: return False
    return True

print('- = land and x = tree\n')
area = [['-' for i in range(30)]for j in range(30)]
trees = 0
while trees < 10:
    x1 = random.randint(0,29)
    y1 = random.randint(0,29)
    if(area[x1][y1] == '-'):
        if check(area, x1, y1):
            area[x1][y1] = 'x'
            trees+=1
for i in range(30):
    print(*area[i])
