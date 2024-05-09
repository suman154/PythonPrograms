# Python Program to Find Largest Element in an Array
# Find largest element in an array Using Native Approach?
def largest(arr, n):

    max = arr[0]

    for i in range (1, n):
        if arr[i] > max:
            max = arr[1]
            return max 
        
arr = [10, 324, 46, 98, 232]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array", Ans)