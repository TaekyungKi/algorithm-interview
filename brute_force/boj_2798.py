import sys
N, M = list(map(int, input().split()))

cards = list(map(int, sys.stdin.readline().strip().split()))

cards.sort()

optimal = 0
bb = False
for i in range(0,len(cards)-2):
    for j in range(i+1,len(cards)-1):
        for k in range(j+1, len(cards)):
            temp = cards[i] + cards[j] + cards[k]
            if optimal < temp <=  M:
               optimal = temp
if optimal > 0:
    print(optimal)