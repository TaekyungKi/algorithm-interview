N = int(input())
assert 1<=N<=1000

d = [0]*1001

d[1] = 1
d[2] = 3

for i in range(3, N+1):
    d[i] = d[i-1] + d[i-2]*2

print(d[N]%796796)