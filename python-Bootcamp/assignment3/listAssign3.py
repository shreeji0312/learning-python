#Shreeji Patel
#105151171

import random
bdays = []

while True:
    date = random.randint(1,365)
    if date in bdays:
        print('Birthdays generated before duplicate: %d' %len(bdays))
        break
    else:
        bdays.append(date)