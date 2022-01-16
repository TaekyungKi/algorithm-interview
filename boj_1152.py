S = str(input().strip())

word_dict = {}

S = S.split()
for word in S:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] +=1
res = 0
for v in word_dict.values():
    res += v
print(res)