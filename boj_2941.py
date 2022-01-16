string = str(input())

alters = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

c = 0
for alter in alters:
    while alter in string:
        string = string.replace(alter, '/', 1)
        c += 1

print(len(string))