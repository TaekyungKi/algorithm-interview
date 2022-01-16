import sys

line = sys.stdin.readline().rstrip()

chars = ["U", "C", "P", "C"]
char_idx = 0
flag = False

while True:
    if char_idx == 4:
        flag = True
        break
    try:
        c = line.index(chars[char_idx])
        line = line[c:]
        char_idx += 1
    except:
        break
if flag:
    print("I love UCPC")
else:
    print("I hate UCPC")