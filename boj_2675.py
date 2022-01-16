T = int(input())
strings = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:'

for i in range(T):
    R, S = input().split()
    R = int(R)
    S = str(S)
    x = ''.join([s*R for s in S])
    print(x)