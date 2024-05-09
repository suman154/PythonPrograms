# Python program to interchange first and last elements in a list
def swaplist(newlist):
    size = len(newlist)


    # swapping
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size - 1] = temp

    return newlist

newlist = [100, 914, 526, 24]

print(swaplist(newlist))

