# #* Python Program to Check Armstrong Number
# def power(x, y):

#     if y ==0:
#         return 1
#     else:
#         if y % 2 ==0:
#             return power(x,y // 2) *power(x,y // 2)
#         return x * power(x,y // 2) * power(x,y // 2)
    
# # function to calculate order of the Number
# def order(x):

#     # variable to store of the Number
#     n = 0
#     while (x != 0):
#         n = n + 1
#         x = x//10

#     return n

# def isArmstrong(x):

#     n = order(x)
#     temp = x
#     sum1 = 0

#     while (temp != 0):
#         r = temp % 10
#         sum1 = sum1 + power(r,n)
#         temp = temp // 10

#         # if condition satisfies
#         return (sum1 == x)
    
# x = 165
# print(isArmstrong(x))

# x = 1245
# print(isArmstrong(x))
   

# #* Python program to check if a number is an Armstrong number without using the power function
# n = 452
# s = n 
# b = len(str(n))

# sum1 = 0
# while n != 0:
#     r = n % 10
#     sum1  = sum1+(r**b)
#     n = n//10
# if s == sum1:
#     print("The given number", s, "is armstrong number")
# else:
#     print("The given number", s ,"is not armstrong number")




# #* Python program to check if a number is an Armstrong number Using string manipulation
# def is_armstrong(num):
#     num_str = str(num)
#     n = len(num_str)
#     sum = 0
#     for digit in num_str:
#         sum += int(digit)**n
#         if sum == num:
#             return True
#         else:
#             return False
        
# num=152
# print(is_armstrong(num))