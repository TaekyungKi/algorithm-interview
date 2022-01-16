N, K = list(map(int, input().split()))

A = []
for _ in range(N):
  A.append(int(input()))

assert len(A) == N

count = 0
for i in range(N):
    t = A[N-1-i]
    if K >= t:
      count += K // t
      K -= (K//t)*t
    else:
      continue
print(count)