N = int(input())

def is_hansoo(n):
    n = str(n)
    if len(n) <= 2:
        return True
    elif len(n) > 2:
        n = str(n)
        d = int(n[0]) - int(n[1])
        hansoo = True
        for i in range(1, len(n)-1):
            d1 = int(n[i]) - int(n[i+1])
            if d == d1:
                continue
            else:
                hansoo = False
                break
        return hansoo
c = 0

for n in range(1, N+1):
    if is_hansoo(n):
        c += 1
print(c)