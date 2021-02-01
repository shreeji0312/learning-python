#Shreeji Patel
#105151171


import random
participants = []

while True:
    person = input('Enter name (x to generate assignments): ')
    if person == 'x' : break

    participants.append(person)


random.shuffle(participants)

for i in range(len(participants)):
    print(participants[i], "gifts", participants[(i+1)%len(participants)])