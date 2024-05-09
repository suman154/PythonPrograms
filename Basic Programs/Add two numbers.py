#* Python program to add two numbers
# Using "+"operator
num1 = 99
num2 = 83

# adding two numbers
sum = num1 + num2

# printing values
print("Sum of", num1, "and", num2, "is", sum)


#* Add Two Numbers with User Input
num1 = input("Enter first number: ")
num2 = input("Enter Second number: ")

# adding two Numbers
sum = float(num1) + float(num2)
# display the value
print("The sum of {0} and {1} is {2}" .format( num1, num2, sum))




#* Add Two Numbers in Python Using Function
def add(a,b):
    return a+b

# initializing the variable
num1 = 78
num2 = 22

# call function and store the result sum of two number
two_numbers = add(num1,num2)
print("The Sum of {} and {} is {}".format(num1,num2, two_numbers))




#* Add Two Number Using Lambda Function
add_numbers = lambda x,y:x+y

# input from user
num1 = 58
num2 = 45

# call lambda Function
result = add_numbers(num1,num2)

# print the result
print("The sum of", num1, "and", num2, "is", result)





#* Add Two numbers using recursion function
def add_recursion(x, y):
    if y == 0:
        return x
    else:
        return add_recursion( x + 1, y - 1 )
    
# input from user
num1 = 34
num2 = 43

# call function
result = add_recursion(num1, num2)

# print result
print("The sum of", num1, "and", num2, "is", result)
    


