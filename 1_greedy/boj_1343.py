line = str(input())
start = 0
while True:
    try:
        c = line[start:].index("XXXX")
    except:
        break
    line_1 = line[:c+start]
    line_3 = line[c+start+4:]
    line = line_1 + "AAAA" + line_3
    start += c+4

start = 0
while True:
    try:
        c = line[start:].index("XX")
    except:
        break
    line_1 = line[:c+start]
    line_3 = line[c+start+2:]
    line = line_1 + "BB" + line_3
    start += c+2
if "X" in line:
    print(-1)
else:
    print(line)