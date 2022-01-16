a, b = list(map(str, input().strip().split() ))

a1 = a[::-1]
b1 = b[::-1]

if a1 >= b1:
    print(a1)
elif a1 < b1:
    print(b1)
