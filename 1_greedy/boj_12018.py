n, m = list(map(int, input().split()))

res = []
for _ in range(n):
    p, L = list(map(int, input().split()))

    m_list = list(map(int, input().split()))
    
    if p < L:
        res.append(1)
    else:
        m_list.sort()
        pp = m_list[-L]
        res.append(pp)

res.sort()
f = 0
c = 0
for i, k in enumerate(res):
    f += k
    if f > m:
        break
    c += 1

print(c)