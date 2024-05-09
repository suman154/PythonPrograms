#* Python Program to Check Prime Number
num = 25

if num > 1:

    for i in range (2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break

    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")



#* Find Prime Numbers with a flag variable
from math import sqrt
n = 2

prime_flag = 0

if (n > 1):
    for i in range (2,int(sqrt(n))+ 1):
        if (n % i ==0):
            prime_flag = 1
            break
        if  (prime_flag == 0):
            print("True")
        else:
            print("False")
    else:
            print("False")



#* Check Prime Numbers Using Recursion
from math import sqrt
def prime(number,itr):
    if itr == 1:
        return True
    if number % itr == 0:
        return False
    if prime(number,itr-1) == False:
        return False
    

    return True

num = 13
itr = int(sqrt(num)+1)
print(prime(num,itr))



#* Check the Prime Trial Division Method
def is_prime_trail_division(n):
    if n <= 1:
        return False
    
    for i in range (2,int(n**0.5)+1):
        if n % i ==0:
            return False
        
    return True

print(is_prime_trail_division(10))




#* Python Program to Check Prime Number Using a while loop to check divisibility
import math

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
        return True
    
print(is_prime(11))
print(is_prime(1))



#* Python Program to Check Prime Number Using Math module
import math
def is_prime(n):
    if  n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) +1):
        if n % i == 0:
            return True
    return True
        
n = 11
print(is_prime(n))



# #* Python Program to Check Prime Number Using sympy.isprime() method
# from sympy import *
 
# # calling isprime function on different numbers
# num1 = isprime(30)
# num2 = isprime(13)
# num3 = isprime(2)
 
# print(num1) # check for 30 is prime or not
# print(num2) # check for 13 is prime or not
# print(num3) # check for 2 is prime or not