def d(n):
    res = n
    for i in str(n):
        res = res + int(i)
    return res
res = list(range(1, 10001))
for i in range(1, 10001):
    t = d(i)
    if t in res:
        res.remove(t)

for i in res:
    print(i)

