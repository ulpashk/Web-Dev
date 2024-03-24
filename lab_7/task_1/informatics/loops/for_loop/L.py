x = input()
summ = 0
n = len(x) #str size
# pow(2, n) 2 to the power n

for i in x:
    b = int(i) * pow(2, n-1)
    n -= 1
    summ += b

print(summ)