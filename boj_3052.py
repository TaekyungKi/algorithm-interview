r_list = []
for i in range(10):
    a = int(input())

    r = a%42
    if r not in r_list:
        r_list.append(r)

print(len(r_list))