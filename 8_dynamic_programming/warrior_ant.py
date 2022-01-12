N = int(input())
assert 3 <= N <= 100
Ks = list(map(int, input().split()))
assert len(Ks) == N
Ks = [0] + Ks

d = [0]*101
d[1] = Ks[1]
d[2] = max(Ks[1], Ks[2]) 

for i in range(3, N+1):
    d[i] = max(d[i-1], d[i-2] + Ks[i])

print(d[N])