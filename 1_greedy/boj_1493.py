"""
    x
"""

import sys
import math

length, width, height = list(map(int, sys.stdin.readline().split()))
N = int(input())

box_list = []
for _ in range(N):
    A, B = list(map(int, sys.stdin.readline().split()))
    box_list.append([A, B])
    
def remainder(ctn, length, width, height, cube):
    cube = 2**cube

    if min(length, width, height) < cube:
        return ctn, length, width, height
    else:
        ctn += (length//cube)*(width//cube)*(height//cube)
        length = length%cube
        width = width%cube
        height = height%cube
    
    return ctn, length, width, height
