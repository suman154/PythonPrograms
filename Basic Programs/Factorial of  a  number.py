# Python Program to Find the Factorial of a Number
#* Find the Factorial of a Number Using Recursive approach?
def factorial(n):

        # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

# deriver code
num = 6
print("Factorial of",num,"is",factorial(num))



# Find the factorial of a Number Using Iterativ approach
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
 
# Driver Code
num = 6
print("Factorial of",num,"is",
factorial(num))


# Example 2:
def factorial(n):
       
    res = 1
      
    for i in range(2, n+1):
        res *= i
    return res
 # Driver Code
num = 6
print("Factorial of", num, "is",
factorial(num))


#* Find the Factorial of a Number Using One line Solution (Using Ternary operator): 
def  factorial(n):
 

        #  single line to find factorial
        return 1 if (n==1 or n==0) else n * factorial(n - 1)

# Driver code
num = 6
print("Factorial of",num,"is",factorial(num))



#* Find the Factorial of a Number Using using In-built function
import math

def factorial(n):
    return(math.factorial(n))

# Driver
num = 6
print("Factoeial of", num, "is", factorial(num))


#* Find the Factorial of a Number Using numpy.prod
import numpy
n=6
x=numpy.prod([i for i in range(1,n+1)])
print(x)



#* Prime Factorization Method to find Factorial
def primeFactors(n):
    factors = {}
    i = 2
    while i*i <= n:
        while n % i == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1
    return factors
 
# Function to find factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n+1):
        factors = primeFactors(i)
        for p in factors:
            result *= p ** factors[p]
    return result
 
# Driver Code
num = 6
print("Factorial of", num, "is", factorial(num))


