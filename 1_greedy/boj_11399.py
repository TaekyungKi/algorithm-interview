import sys

N = int(input())

data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()

res = 0
for i, d in enumerate(data):
    res += d*(len(data)-i)

print(res)
