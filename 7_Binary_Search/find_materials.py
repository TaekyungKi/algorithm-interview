import sys

N = int(input())
given = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(input())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

# binary search
given.sort()

def binary_search(given, target, start, end):
    



# linear search
# for i, t in enumerate(target):
#     if t in given:
#         print('yes', end = ' ')
#     else:
#         print('no', end = ' ')
