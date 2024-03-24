import sys
n = int(input())
i = 1

while i != n:
    if i > n:
        print("NO")
        sys.exit()
    i *= 2

print("YES")