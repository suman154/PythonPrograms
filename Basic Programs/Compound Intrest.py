# Python Program for Compound Interest
#*Find Compound Interest with Python
def compound_intrest(principle, rate, time):

    # calculate compound intrest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound intrest is", CI)


compound_intrest(10000, 12.5,8)


#*Compound Interest with Input taking from user

def compound_intrest(principal, rate, time):

    # calculation compound intrest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound intrest is",CI)



# Taking input from user
principal = int(input("Enter the principal amount :"))
rate = int(input("Enter rate of intrest :"))
time = int(input("Enter time in years :"))

# function callable

compound_intrest(principal,rate,time)


#* Finding compound interest of given values without using pow() function.
p= 10000
t= 3
r= 10.5

# calculate compound intrest
a=p*(1+(r/100))**t
ci=a-p

# print compound intrest
print(ci)


#* Compound intrest using for loop
def compound_intrest(principal, rate, time):
    Amount = principal
    for i in range(time):
        Amount = Amount * (1 + rate/100)

    CI = Amount - principal
    print("Compound intrest is",CI)

    
compound_intrest(1500, 5.8, 5)








