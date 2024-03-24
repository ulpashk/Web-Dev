import math
n = int(input())
i = 1

while i <= n:
    if int(math.sqrt(i)) == math.sqrt(i):
        print(i)
    i += 1