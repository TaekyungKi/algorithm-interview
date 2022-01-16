N = int(input())

if N < 10:
    N = 10*N

c = 0
while True:
    if c == 0:
        k = N
    a = k//10
    b = k%10
    x = a + b
    k = b*10+x%10
    c += 1
    if k == N:
        break
print(c)