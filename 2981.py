# 검문

import sys
from math import gcd, sqrt

N = int(input())

bn = int(sys.stdin.readline())
bg = 0
for _ in range(N-1):
    n = int(sys.stdin.readline())
    if bg == 0: bg = abs(bn-n)
    else: bg = gcd(bg, abs(bn-n))
    bn = n

S = []
for i in range(2, int(sqrt(bg))+1):
    if bg%i == 0: S.append(i)

if S: print(*S, end=' ')
for n in S[::-1]:
    if n**2 != bg: print(bg//n, end=' ')
print(bg)