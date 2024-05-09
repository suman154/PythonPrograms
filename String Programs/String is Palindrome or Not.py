# Python Program to Check if a String is Palindrome or Not
def isPalindrome(s):
    return s == s[::-1]

# Driver Code
s =  "Computer"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")