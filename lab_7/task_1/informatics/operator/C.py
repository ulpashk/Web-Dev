a = int(input())
b = int(input())

if a == 1:
    if b == 1:
        print("YES")
    else:
        print("NO")
elif a != 1:
    if b != 1:
        print("YES")
    elif b == 1:
        print("NO")