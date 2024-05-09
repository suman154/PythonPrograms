#* Program to print ASCII Value of a character
c = 'g'
print("The ASCII value of '" + c+ "'  is:", ord(c))


#* Here is a method to print the ASCII value of the characters in a string using python:
print("Enter a String: ", end="") 
text = input() 
textlength = len(text) 
for char in text: 
    ascii = ord(char) 
    print(char, "\t", ascii)