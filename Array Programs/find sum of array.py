#* Python Program to Find Sum of Array
def _sum(arr):
 
    # initialize a variable
    sum = 0
 
    # iterate through the array
    for i in arr:
        sum = sum + i
 
    return(sum)
 
 
# main function
if __name__ == "__main__":
    # input values to list
    arr = [12, 3, 4, 15]
 
    # calculating length of array
    n = len(arr)
    # calling function ans store the sum in ans
    ans = _sum(arr)
    # display sum
    print('Sum of the array is ', ans)
