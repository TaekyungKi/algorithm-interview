A, B, C = list(map(int, input().split()))

if B >= C:
    print(-1)
elif B < C:
    N = int(A//(C-B)) + 1
    print(N)