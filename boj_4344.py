import sys

C = int(input())

for _ in range(C):
    line = list(map(int, sys.stdin.readline().split()))
    N = line[0]
    ave = sum(line[1:])/N
    
    upper = 0
    for s in line[1:]:
        if s > ave:
            upper += 1
    print(f"{100*(upper/N):2.3f}%")