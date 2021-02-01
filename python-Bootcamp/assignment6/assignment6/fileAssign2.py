#Shreeji Patel
#105151171

people = open('people.txt', 'r')
names = open('names.txt', 'w')
hobbies=[]
people_read = people.read()
people_list = people_read.strip().split('\n')

temp_list = []
for i in range(len(people_list)):
    temp_list.append(people_list[i].split(','))

for i in range(len(temp_list)):
    names.write(temp_list[i][0]+'\n')
    if temp_list[i][1] not in hobbies:
        hobbies.append(temp_list[i][1])
    if temp_list[i][2] not in hobbies:
        hobbies.append(temp_list[i][2])
    if temp_list[i][3] not in hobbies:
        hobbies.append(temp_list[i][3])

temp = hobbies[:]
for i in range(len(hobbies)):
    hobbies[i] = hobbies[i]+'.txt'
    hobbies[i] = open(hobbies[i], 'w')


for i in range(len(temp_list)):
    for j in range(len(hobbies)):
        if(temp[j] == temp_list[i][1]):
            hobbies[j].write(temp_list[i][0]+'\n')
        if(temp[j] == temp_list[i][2]):
            hobbies[j].write(temp_list[i][0]+'\n')
        if(temp[j] == temp_list[i][3]):
            hobbies[j].write(temp_list[i][0]+'\n')            

for i in range(len(hobbies)):
    hobbies[i].close()

