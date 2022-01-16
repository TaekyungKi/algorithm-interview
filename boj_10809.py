S = str(input())

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i, a in enumerate(alphabet):
    if a in S:
        print(S.index(a), end = ' ')
    else:
        print(-1, end = ' ')
