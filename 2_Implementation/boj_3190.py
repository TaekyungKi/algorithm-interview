N = int(input())
K = int(input())

d = [ [0]*(N+1) for _ in range(N+1) ]

# current
x, y = 1, 1

n = (-1, 0)
e = (0, 1)
s = (1, 0)
w = (0, -1)

l_dict = {'e': 'n', 'n': 'w', 'w': 's', 's': 'e'}
r_dict = {'e': 's', 's': 'w', 'w': 'n', 'n': 'e'}
dd = {'e': e, 'n': n, 's': s, 'w': w}


current_d = e
# 빈칸: 0, 사과:1
for k in range(K):
    i, j = list(map(int, input().split()))
    d[i][j] = 1

L = int(input())
l_change = []

for i in range(L):
    u1, u2 = list(input().split())
    l_change.append([int(u1), u2])

t = 0
cc = 0

while True:
    if t == l_change[cc][0]:
        if l_change[cc][1] == 'L':
            current_d = dd.get(l_dict.get(current_d))
            cc += 1
        else:
            current_d = dd.get(r_dict.get(current_d))
            cc += 1

    x_t = x + current_d[0] 
    y_t = y + current_d[1]

    if x == N+1 or x == 0 or y == N+1 or y == 0:
        break

    if d[x_t][y_t] == 1:
        
    
    t += 1
    