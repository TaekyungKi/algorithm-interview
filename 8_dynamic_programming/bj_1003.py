T = int(input())

for _ in range(T):
    N = int(input())
    assert 0 <= N <= 40
    if N == 0:
        print(1, 0)
        continue
    if N == 1:
        print(0, 1)
        continue
    if N == 2:
        print(1, 1)
        continue

    # d[i] = [i번째 피보나치 수, i번째까지 0이 불린 횟수, i번째까지 1이 불린 횟수]
    d = [[0,0,0] for _ in range(N+1)]
    d[0] = [0, 1, 0]
    d[1] = [1, 0, 1]
    d[2] = [2, 1, 1]
    
    for i in range(2, len(d)):
        d[i][0] = d[i-1][0] + d[i-2][0]
        d[i][1] = d[i-1][1] + d[i-2][1]
        d[i][2] = d[i-1][2] + d[i-2][2]

    print(d[N][1], d[N][2])