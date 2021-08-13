# 크냐?

from sys import stdin

A, B = map(int, stdin.readline().split())
while A != 0 or B != 0:
    if A > B: print('Yes')
    else: print('No')

    A, B = map(int, stdin.readline().split())