# -*- coding: utf-8 -*-
"""
    입력 조건: N (2 <= N <= 1000), M(1 <= M <= 10000), K (1 <= K <= 10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
            둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10000이하의 수로 주어진다.
            입력으로 주어지는 K는 항상 M보다 작거나 같다.
    출력 조건: 더해진 답을 출력한다.
"""

N, M, K =  map(int, input().split())

xx = list( map(int, input().split()))
assert len(xx) == N

xx.sort()
max1 = xx[-1]
max2 = xx[-2]

res = 0
step = 1
while step <= M:
    for j in range(K):
        res += max1
        step += 1

        if j == K-1:
            res += max2
            step += 1

        if step >= M:
            break
print(res)

"""
    Conclusion: 이게 왜 그리디일까? 더하는 값을 x라고 했을 때, 그 x는 매 순간에 선택할 수 있는 "가장 큰 값"이다. 매 순간마다 더하는 값의 "조건"이 달라지지 않는다면, 결과는 단순한 constant 값으로 나오며
                문제로 출제되는 경우엔 그 조건의 규칙을 파악해서 코드로 구현할 수 있는 지를 보는 것 같다.
"""