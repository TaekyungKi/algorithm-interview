N = int(input())


def is_checker(text):
    already = []
    checker = True
    for i, t in enumerate(text):
        if i == 0:
            already.append(t)
        else:
            if t in already:
                if t == already[-1]:
                    already.append(t)
                elif t != already[-1]:
                    checker = False
                    break
            elif t not in already:
                already.append(t)
    return checker

res = 0
for i in range(N):
    text = str(input())
    checker = is_checker(text)
    if checker:
        res += 1
        
print(res)