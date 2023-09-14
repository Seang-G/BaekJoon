# 정수 삼각형

import sys

n = int(input())

O = [0]
for i in range(n):
    N = list(map(int, sys.stdin.readline().split()))
    N[0] += O[0] 
    for j in range(1, i):
        N[j] += max(O[j], O[j-1])
    N[-1] += O[-1]
    O = N

print(max(O))