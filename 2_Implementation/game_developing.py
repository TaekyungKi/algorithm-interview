"""
    난이도: 중 | 풀이 시간: 40min | 시간 제한: 1s | 메모리 제한: 128MB
"""

N, M = list(map(int, input().split()))
A, B, d = list(map(int, input().split()))

rr = []
for n in range(N):
  row = list(map(int, input().split()))
  rr.append(row)

count = 0

direction = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
d_chain = {0: 3, 3: 2, 2: 1, 1: 0}

no_where = 0
while True:
  if no_where == 4:
    
    break
  d_1 = d_chain.get(d)
  dx, dy = direction[d_1]
  t_x, t_y = A + dx, B + dy
  if 0<= t_x < N and 0 <= t_y < M:
    if rr[t_x][t_y] == 0:
      rr[A][B] = 2
      A, B = t_x, t_y
      d = d_1
      count += 1
      no_where = 0
    elif rr[t_x][t_y] == 1:
      no_where +=1
      d = d_1
      continue
    elif rr[t_x][t_y] == 2:
      no_where += 1
      d = d_1
      continue
  else:
    no_where += 1
    d = d_1
    continue
print()
for i in rr:
  for k,j in enumerate(i):
    if k != M-1:
      print(j, end=' ')
    else:
      print(j)
print(count)