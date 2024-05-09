#* Python Program to Print all Prime numbers in an Interval
def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:     
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
 
# Driver program
starting_range = 2
ending_range = 7
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)




#* Optimized way to find a Prime Number
def prime(starting_range, ending_range):
  lst=[]
  flag=0                   #Declaring flag variable
  for i in range(starting_range, ending_range):#elements range between starting and ending range 
    for j in range(2,i):  
      if(i%j==0):     #checking if number is divisible or not
        flag=1        #if number is divisible, then flag variable will become 1
        break
      else:
        flag=0     
    if(flag==0):    #if flag variable is 0, then element will append in list  
      lst.append(i)
  return lst
 
# Driver program
starting_range = 2
ending_range = 7
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)



#* Sieve of Eratosthenes Method:
import math
 
def SieveOfEratosthenes(srt, n):
    # Create a boolean array "prime[srt to n]" and
    # initialize all entries it as true. A value in
    # prime[i] will finally be false if i is Not a prime,
    # else true.
    prime = [True for i in range(n + 2 - srt)]
    prime[0] = False
    prime[1] = False
 
    for p in range(srt, int(math.sqrt(n))+1):
        # If prime[p] is not changed, then it is a prime
        if prime[p] == True:
            # Update all multiples of p greater than or
            # equal to the square of it numbers which are
            # multiple of p and are less than p^2 are
            # already been marked.
            for i in range(p*p, n+1, p):
                prime[i] = False
 
    # Print all prime numbers
    for p in range(srt, n+1):
        if prime[p]:
            print(p, end=" ")
 
# Driver Code
if __name__ == "__main__":
    srt = 1
    end = 10
    SieveOfEratosthenes(srt, end)


#* Optimized Sieve of Eratosthenes Method: (Bitwise Sieve Method)
def bitwiseSieve(srt, n):
 
    # prime[i] is going to store
    # true if if i*2 + 1 is composite.
    prime = [0]*int(n / 2);
 
    # 2 is the only even prime so
    # we can ignore that. Loop
    # starts from 3.
    if (srt%2 == 0):
        srt += 1
    if(srt <= 2):
        srt = 3
    i = srt
    while(i * i < n):
        # If i is prime, mark all its
        # multiples as composite
        if (prime[int(i / 2)] == 0):
            j = i * i;
            while(j < n):
                prime[int(j / 2)] = 1;
                j += i * 2;
        i += 2;
 
    # writing 2 separately
    print(2,end=" ");
 
    # Printing other primes
    i = 3;
    while(i < n):
        if (prime[int(i / 2)] == 0):
            print(i,end=" ");
        i += 2;
 
 
# Driver code
if __name__=='__main__':
    srt = 1
    end = 10
    bitwiseSieve(srt, end)