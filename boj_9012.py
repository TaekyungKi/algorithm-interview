T = int(input())

for t in range(T):
    PS = str(input())
    x = []

    for t in PS:
        if t == '(':
            x.append(t)

        elif t == ')':
            if '(' in x:
                x.pop()
            else:
                x.append(')')
                break

    if len(x) > 0:
        print("NO")
    elif len(x) == 0:
        print("YES")