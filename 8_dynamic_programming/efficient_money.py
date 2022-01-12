N, M = list(map(int, input().split()))
money_list = []
for i in range(N):
    money_list.append(int(input()))

d = [0] + [10001]*M

for money in money_list:
    for i in range(1, M+1):
        try:
            if d[i-money] != 10001:
                if i - money > 0:
                    d[i] = min(d[i], d[i-money]+1)
        except:
            pass

if d[M] == 10001:
    print("-1")
else:
    print(d[M])

"""
    1. 초기화를 반드시 0으로 할 필요는 없다. 엄청나게 큰 숫자를 이용해도 된다.
    2. 화폐, 칸 수 단위 등은 sorting 하지 않아도 된다. -> 매 iteration 마다 조건을 만족하는 것으로 재 할당하도록 만들 수 있다.
    3. try: process.... except: pass 를 가능한 경우에만 설정하고, 안되는 경우는 그냥 초깃값을 내보내도록 할 수 있다.
    4. list는 length 보다 큰 경우에만 index error가 난다.
    5. list는 음수 index도 가능하다.
"""