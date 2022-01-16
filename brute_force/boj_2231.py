N = int(input())

def generator(n):
    res = n
    if n >=10:
        for k in str(n):
            res += int(k)
        return res
    elif 1<= n <=9:
        return 2*res

for n in range(1, N+1):
    gen_n = generator(n)
    if gen_n == N:
        ans = n
        break
    else:
        ans = 0
print(ans)