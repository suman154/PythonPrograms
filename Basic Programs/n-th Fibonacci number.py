#* Python Program for n-th Fibonacci number Using recursion
def fabonacci(n):
    if n<= 0:
        print("Incorrect input")

    elif n == 1:
        return 0
    
    elif n == 2:
        return 1
    
    else:
        return fabonacci(n - 1) + fabonacci(n - 2)


print(fabonacci(15))



#* Python Program for n-th Fibonacci number Using Dynamic Programming 
FibArray = [0,1]

def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n<= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = Fibonacci(n-1)+Fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib
    
print(Fibonacci(9))



#* n-th Fibonacci number Using Dynamic Programming with Space Optimization
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
 

 
print(fibonacci(9))



#* Python Program for n-th Fibonacci number Using Using Arrays 
def fibonacci(n):
    if n <= 0:
        return "Incorrect Output"
    data = [0, 1]
    if n > 2:
        for i in range(2, n):
            data.append(data[i-1] + data[i-2])
    return data[n-1]
 

print(fibonacci(9))



#* Python Program for n-th Fibonacci number Using Direct Formula 
from math import sqrt 
# import square-root method from math library
def nthFib(n):
    res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
    # compute the n-th fibonacci number
    print(int(res),'is',str(n)+'th fibonacci number')
    # format and print the number
     
# driver code
nthFib(12)
 

#* Python Program for n-th Fibonacci number Using power of the matrix {{1, 1}, {1, 0}}
def fib(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)
    return F[0][0]
 
 
def multiply(F, M):
  x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])
  y = (F[0][0] * M[0][1] + F[0][1] * M[1][1])
  z = (F[1][0] * M[0][0] + F[1][1] * M[1][0])
  w = (F[1][0] * M[0][1] + F[1][1] * M[1][1])
  F[0][0] = x
  F[0][1] = y
  F[1][0] = z
  F[1][1] = w
 
 
def power(F, n):
    M = [[1, 1], [1, 0]]
    # n - 1 times multiply the
    # matrix to {{1,0},{0,1}}
    for i in range(2, n + 1):
        multiply(F, M)
 
 
# Driver Code
if __name__ == "__main__":
    n = 9
    print(fib(n))
 


