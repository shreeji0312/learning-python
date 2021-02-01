#Shreeji Patel
#105151171

def collide(grid1, grid2):
    for numberList1 in grid1:
        for numberList2 in grid2:
            for number1 in numberList1:
                for number2 in numberList2:
                    if(number1 == 1 & number2 == 1):
                        return True
    return False


'''
grid1 = [[0,0,0,0],[0,1,0,0],[0,0,0,0]]
grid2 = [[0,0,0,0],[0,1,0,0],[0,0,0,0]]
print(collide(grid1, grid2))
'''