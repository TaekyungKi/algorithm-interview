N, M = list(map(int, input().split()))

src = [0 for _ in range(N)]

for row in range(N):
    src[row] = [ t for t in str(input())]
rev = {"B": "W", "W": "B"}
min_act = 64

basic = [["B", "W", "B", "W", "B", "W", "B", "W"],
        ["W", "B", "W", "B", "W", "B", "W", "B"]]

ans1 = basic + basic + basic + basic
basic = basic[::-1]
ans2 = basic + basic + basic + basic

for i in range(N-8+1):
    for j in range(M-8+1):
        sub = [t[j:j+8] for t in src]
        sub = sub[i:i+8]    
        c1, c2 = 64, 64
        
        for k in range(8):
            for l in range(8):
                if sub[k][l] != ans1[k][l]:
                    c1 -= 1
                if sub[k][l] != ans2[k][l]:
                    c2 -= 1
        min_act = min(min_act, c1, c2)
print(min_act)

"""
for i in range(N-8+1):
    for j in range(M-8+1):
        sub = [t[j:j+8] for t in src]
        sub = sub[i:i+8]
        c = 0
        for k in range(8):
            for l in range(8):
                if k == 0 and l == 0:
                    continue
                elif k == 0 and l != 0:
                    if sub[k][l-1] == sub[k][l]:
                        sub[k][l] = rev.get(sub[k][l])
                        c += 1
                elif k != 0 and l == 0:
                    if sub[k-1][l] == sub[k][l]:
                        sub[k][l] = rev.get(sub[k][l])
                        c += 1
                elif k != 0 and l != 0:
                    if sub[k-1][l-1] != sub[k][l]:
                        sub[k][l] = rev.get(sub[k][l])
                        c += 1
        if c < min_act:
            print(sub)    
            min_act = c
print(min_act)
"""