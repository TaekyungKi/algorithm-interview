N = int(input())

a = [[0]*3]
for _ in range(N):
    a.append(list(map(int, input().split())))

if N == 1:
    print(min(a[1]))
else:
    for i in range(2, len(a)):
        a[i][0] += min(a[i-1][1], a[i-1][2])
        a[i][1] += min(a[i-1][0], a[i-1][2])
        a[i][2] += min(a[i-1][0], a[i-1][1])

    print(min(a[-1]))