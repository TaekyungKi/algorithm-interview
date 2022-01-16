import sys

N = int(input())

scores = list(map(int, sys.stdin.readline().split()))

max_score = max(scores)

new_scores = [(100*t/max_score) for t in scores]

print(sum(new_scores)/N)