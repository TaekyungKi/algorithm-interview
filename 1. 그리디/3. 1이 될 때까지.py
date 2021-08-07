# -*- coding: utf-8 -*-
"""
    입력조건: 첫째 줄에 N (2 <= N <= 100000)과 K (2 <= K <= 100000)가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.
    출력조건: 첫째 줄에 N이 될 때까지 1번 혹은 2번의 과정을 수행해야하는 횟수의 최솟값을 출력한다.
"""

N, K = list(map(int, input().split()))

count = 0
if K == 1:
  while True:
    N -= 1
    count += 1
    if N == 1:
      break
else:
  while True:
      if N % K == 0:
          N /= K
      else: 
          N -= 1
      count += 1

      if N == 1:
          break
print(count)