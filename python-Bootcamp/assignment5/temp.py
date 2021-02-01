#Shreeji Patel
#105151171

import random
import math


def check():
    trees = []
    test = []
    for i in range(10):
        x = random.randint(1,30)
        y = random.randint(1,30)
        trees.append([x,y])
    for point1 in trees:
        test = trees[:]
        test.remove(point1)
        for point2 in test:
            x1 = point1[0] 
            x2 = point2[0]
            y1 = point1[1]
            y2 = point2[1]
            x = (x2-x1)**2
            y = (y2-y1)**2
            d = math.sqrt(x+y)
            if d < 3:
                check()
                break
    return trees


print(check())