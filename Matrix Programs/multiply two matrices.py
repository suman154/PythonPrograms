# Program to multiply two matrices using list comprehension

A = [[10, 7, 3]
     [4, 5, 6]
     [7, 8, 9]]


B = [[5, 8, 1, 3]
     [6, 7,4, 9]
     [4, 5,76,7]]

result = [[sum(a * b for a, b in zip(A_row, B_col)) 
                        for B_col in zip(*B)]
                                for A_row in A]

for r in result:
    print(r)