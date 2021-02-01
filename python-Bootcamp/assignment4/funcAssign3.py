#Shreeji Patel
#105151171


def lowestCommonMultiple(x, y):
   if x > y : grt = x
   else : grt = y

   while(True):
       if((grt % x == 0) and (grt % y == 0)):
           lcm = grt
           break
       grt += 1

   return lcm

#print(lowestCommonMultiple(7,5))
