T = int(input())

for _ in range(T):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    elif 3 < n:
        d = [0]*(n+1)
        d[1] = 1
        d[2] = 2
        d[3] = 4
        
        for i in range(4, len(d)):
            d[i] = d[i-1] + d[i-2] + d[i-3]
        
        print(d[n])

"""
    1. 복잡해 보이는 수열이라도 나열을 해보면 간단한 경우가 많음.
    2. n=1, n=2 등 initialization은 필히 실수 없이 하되,
       그 다음 few case는 계산을 몇번 해보면 규칙을 파악 할 수 있음.
    3. 그래서 사실 점화식만 알아내면 DP 문제는 바로 풀 수 있을 것으로 생각됨.
"""