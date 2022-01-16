N = int(input())

c = 0
i = 0
while True:
    if '666' in str(i):
        c += 1    
    if c == N:
        res = i
        break
    i += 1

print(res)