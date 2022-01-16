N = int(input())

d = []
for i in range(N):
    d.append(tuple(map(int, input().split())))

res = [1]*N
for i, (x0, y0) in enumerate(d):
    for (x1, y1) in d:
        if x0 < x1 and y0 < y1:
           res[i] += 1
for t in res:
    print(t, end = ' ') 