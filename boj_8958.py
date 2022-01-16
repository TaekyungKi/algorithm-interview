N = int(input())

for _ in range(N):
    line = str(input())
    score_list = []

    for i, l in enumerate(line):
        if i == 0:
            if l == 'O':
                score_list.append(1)
            else:
                score_list.append(0)
        else:
            if l == 'O':
                if line[i-1] == 'O':
                    score_list.append(score_list[i-1] + 1)
                elif line[i-1] == 'X':
                    score_list.append(1)
            elif l == 'X':
                score_list.append(0)

    print(sum(score_list))