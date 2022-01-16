alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

max_count = 0

S = str(input()).upper()
t = []
max_val = [0]
for i, a in enumerate(alphabets):
    s = S.count(a)
    t.append(s)
    if s >= max_val[-1]:
        max_val.append(s)
        max_char = a

if max_val[-1] == max_val[-2]:
    print('?')
else:
    print(max_char)