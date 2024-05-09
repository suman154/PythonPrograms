# Python program to read file word by word
with open('D:/Python With Django/Python Programs/File Handling Programs/demo.txt','r') as file:
  
    # reading each line    
    for line in file:
  
        # reading each word        
        for word in line.split():
  
            # displaying the words           
            print(word)