n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
elif n >= 3:
    d = [0]*(n+1)
    d[1] = 1
    d[2] = 2
    for i in range(3, len(d)):
        d[i] = d[i-1] + d[i-2]

    print(d[n]%10007)