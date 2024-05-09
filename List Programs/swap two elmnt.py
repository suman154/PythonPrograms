# Python Program to Swap Two Elements in a List
# Swap Two Elements in a List using comma assignment 
def swapPosition(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

list = [23, 58, 35, 97]
pos1, pos2 = 1, 3

print(swapPosition(list, pos1-1, pos2-2))
