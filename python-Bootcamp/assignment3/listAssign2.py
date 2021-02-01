#Shreeji Patel
#105151171

listmonth = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = int(input('Month: '))
day = int(input('Day: '))
totaldays = 0

for i in range(month-1):
    totaldays += listmonth[i]

totaldays += day
print('That\'s day %d of the year' %totaldays)