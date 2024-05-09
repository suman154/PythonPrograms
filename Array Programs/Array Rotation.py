# 3. Python Program for array rotation
def reverse(start, end, arr):
    no_of_reverse = end-start+1
    count =0
    while((no_of_reverse)//2 != count):
        arr[start+count], arr[end-count] = arr[end-count], arr[start+count]
        count += 1
        return arr
    
# length of array and no of rotation 
def left_ratate_array(arr, size, d):
    # Reverse the list
    start = 0
    end = size-1
    arr = reverse(start, end, arr)

    # Divide array into sub-array
    start = 0
    end = size-d-1
    arr = reverse(start, end, arr)
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = 10
d = 1
print('Original array:', arr)

# All Symmetric rotations number
if(d <= size):
    print ('Rotated array: ', left_ratate_array(arr, size, d))
else:
    d = d % size
    print('Rotated array: ', left_ratate_array(arr, size, d))




# Python Program for Array Rotation Using temp array
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1

    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d  + 1
    arr[:] = arr[: i] + temp
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]        
print("Array after left rotation is: ", end= ' ')
print(rotateArray(arr, len(arr), 2))





# Python Program for Array Rotation Using Rotate one by one
def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)


def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
        arr[n-1] = temp


def printArray(arr, size):
    for i in range(size):
        print ("%d"% arr[i], end=" ")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
leftRotate(arr, 2, 9)
printArray(arr, 9)



# Python Program for Array Rotation Using 4 Juggling Algorithm
def leftRotate(arr, d, n):
    for i in range(abc(d, n)):
 
        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
 
# UTILITY FUNCTIONS
# function to print an array
 
 
def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")
 
# Function to get abc of a and b
 
def abc(a, b):
    if b == 0:
        return a
    else:
        return abc(b, a % b)
 
 
# Driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
leftRotate(arr, 2, 9)
printArray(arr, 9)



# Another Approach : Using List slicing
def rotateList(arr,d,n):
    arr[:]=arr[d:n]+arr[0:d]
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr)
print('Rotaetd List is')
print(rotateList(arr,3,len(arr)))