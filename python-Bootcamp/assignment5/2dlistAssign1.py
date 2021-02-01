#Shreeji Patel
#105151171

def empty(list):
    for numberlist in list:
        for number in numberlist:
            if(number != 0 ):
                return False
    return True


def find(list, test):
    flag = True
    column = 0
    for numberlist in list:
        row = 0
        for number in numberlist:
            if(number == test):
                flag = False
                return([column,row])
            row +=1
        column+=1
    if(flag == True):
        return [-1,-1]

                
    

'''grid1 = [[23,34,45],[44,67,3],[7,8,9]]
grid2 = [[0,0,0,0,0],[0,0,0,0,],[0,0,0,0,0]]
print(empty(grid2))
find(grid1, 67)
'''