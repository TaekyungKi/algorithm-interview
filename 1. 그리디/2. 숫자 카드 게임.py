# -*- coding: utf-8 -*-
"""
    입력조건: 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주여진다.
            둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10000 이하의 자연수이다.
    출력조건: 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
"""
N, M = map(int, input().split())

matrix = []
for i in range(N):
  temp = list(map(int, input().split()))
  assert len(temp) == M, print("should be same length")
  matrix.append(temp)

_res = 0
for i in range(N):
  temp_min = min(matrix[i])
  _res = max(_res, temp_min)

print(_res)