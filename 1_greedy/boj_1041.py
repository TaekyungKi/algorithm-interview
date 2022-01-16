import sys

N = int(input())

dice_list = list(map(int, sys.stdin.readline().split()))
dice_list_value = dice_list.sort()

if N == 1:
    res = sum(dice_list) - max(dice_list)

if N == 2:
    dice_max = dice_list[-1]
    dice_min = dice_list[0]
    dice_list_value = dice_list_value[1:-1]
    