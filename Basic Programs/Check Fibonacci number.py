#* Python Program for How to check if a given number is Fibonacci number?
import math

def isPerfectSqure(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFabonacci(n):
    return isPerfectSqure(5*n*n+4) or isPerfectSqure(5*n*n - 4)

for i in range(1, 100):
    if (isFabonacci(i) == True):
        print(i, "is a fabonacci Number")
    else:
        print(i, "is not a fabonacci Number")