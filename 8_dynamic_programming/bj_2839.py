N = int(input())
assert 3 <= N <= 5000

d = [5000]*(N+1)
if N >= 3:
    d[3] = 1
if N >= 5:
    d[5] = 1

for i in range(3, N+1):
    if i - 3 > 0:
        d[i] = min(d[i-3] + 1, d[i])

    if i - 5 > 0:
        d[i] = min(d[i-5] + 1, d[i])

if d[N] == 5000:
    print(-1)
else:
    print(d[N])