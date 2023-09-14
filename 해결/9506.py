# 약수들의 합

import math
from sys import stdin

n = int(stdin.readline())
while n != -1:
    S = set([1])
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            S.add(i)
            S.add(n//i)

    S = list(S)
    S.sort()
    if sum(S) == n:
        print(f'{n} =', end=' ')
        print(*S, sep=' + ')
    else: print(f'{n} is NOT perfect.')

    n = int(stdin.readline())