# 부호

from sys import stdin

for _ in range(3):
    N = int(input())
    S = 0
    for __ in range(N):
        S += int(stdin.readline().strip())
    if S > 0: print('+')
    elif S < 0: print('-')
    else: print('0')