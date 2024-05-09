#* Python Program for cube sum of first n natural numbers
def sumofSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i*i

    return sum

n = 3
print(sumofSeries(n))