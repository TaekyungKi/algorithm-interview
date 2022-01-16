import sys

T = int(input())

for _ in range(T):
    N = int(input())
    cards = list(sys.stdin.readline().rstrip().split())
    res = cards[0]
    cards = cards[1:]
    for c in cards:
        if c <= res[0]:
            res = c + res
        else:
            res = res + c
    print(res)