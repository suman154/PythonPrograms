#* Maximum of two numbers in Python
# Find Maximum of two numbers in Python using if-else statement
def Maximum(x, y):

    if x >= y:
        return x
    else:
        return y 
    
# Driver code
x = 32
y = 76

print(Maximum(x, y))



#* Find maximum number using max() function
x = 32
y = 76

maximum = max(x, y)
print(maximum)

#* Maximum of two number using Ternary operator
x = 32
y = 76

# use ternary operator
print(x if x >=y else y)


#* Maximum of two numbers Using lambda function 
a=5;b=6
maximum = lambda a,b:a if a > b else b 
print(f'{maximum(a,b)} is a maximum number')


#* Maximum of two numbers using list comperehension
a=5;b=8
x=[a if a>b else b]
print("The maximum number is:",x)

#* Maximum of two numbers usig sort() method
a = 4
b = 9
x=[a,b]
x.sort()
print(x[-1])

