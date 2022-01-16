N = int(input())

if N == 1:
    print(1)
elif N >= 2:
    d = [0]*(N+1)
    d[1] = 1
    for i in range(2, N+1):
        d[i] = 2*d[i-1] + 1
    print(d[N])