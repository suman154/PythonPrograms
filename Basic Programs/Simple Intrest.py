# Python Program to Find the Factorial of a Number
#* Find the Factorial of a Number Using Recursive approach
def simple_intrest(p,t,r):
    print('The principle is',p)
    print('The time period is',t)
    print('The rate of intrest is',r)

    si = (p * t * r)/100
    print('The simple intrest is', si)
    return si

simple_intrest(1000,8,12)



#* Program for simple interest with Taking input from user
def simple_intrest(p,t,r):
    print('The principle is',p)
    print('The time period is',t)
    print('The rate of intrest is',r)

    si = (p * t * r)/100
    print('The simple intrest is', si)

P = int(input("Enter the principle amount :"))
T = int(input("Enter the time period :"))
R = int(input("Enter the rate of intrest :"))

simple_intrest(P,T,R)