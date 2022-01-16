import sys

N = int(input())

d = [[0,0] for _ in range(N+1)]
k = [0 for _ in range(N+1)]

for i in range(N):
    d[i] = list(map(int, sys.stdin.readline().rstrip().split()))

    