N = int(input())
if N == 1:
    print(0)
    
else:
    d = [0]*(N+1)
    d[2] = 1
    for i in range(2, len(d)):
        d[i] = d[i-1] + 1
        if i % 3 == 0:
            d[i] = min(d[i], d[i//3] + 1)
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2] + 1)
    print(d[-1])


"""
    1. for문을 돌 때는 initialization을 고려해서 시작점과 끝점을 잘 선택한다.
"""