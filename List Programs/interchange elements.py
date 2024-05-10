# 1. Python program to interchange first and last elements in a listelements in a list
# Approach 1:
def swaplist(newlist):
    size = len(newlist)
    # swapping
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size - 1] = temp

    return newlist

newlist = [100, 914, 526, 24]

print(swaplist(newlist))



# Approach 2:
def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList
     
newList = [10, 20, 30, 40, 222]
print(swapList(newList))



# Approach :3
def swapList(list):
    get = list[-1], list[0]

    list[0], list[-1] = get

    return list

newList = [10, 20, 30, 40, 50]
print(swapList(newList))


# Approach :4
list = [2, 3, 5, 4, 9, 6, ]

a, *b, c = list

print(a)
print(b)
print(c)



# Approach :5
def swapList(list):

    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)
    list.append(first)

    return list 

newlist =[10, 56,78, 79, 26]
print(swapList(newlist))



# Approach : 6 Using Slicing
def swap_first_last_3(lst):
    if len(lst) >= 2:
        lst = lst[-1:] + lst[1:-1] + lst[:1]
    return lst 

inp=[15, 45, 79, 61, 31, 16]
print("The original input is:", inp)

result=swap_first_last_3(inp)

print("The output after swap first and last is:", result)