# Python program to find the sum of all items in a dictionary. 
#Method 1: Using Inbuilt sum() Function
def returnSum(myDict):

    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)

    return final 
    
dict = {'a': 200, 'b': 300, 'c': 500}
print("Sum :", returnSum(dict))