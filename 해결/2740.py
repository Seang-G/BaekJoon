# 행렬 곱셈

from sys import stdin
from functools import reduce

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, stdin.readline().split())))

M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, stdin.readline().split())))

B = list(zip(*B))

for lstA in A:
    for lstB in B:
        S = 0
        for i in range(len(lstA)):
            S += lstA[i] * lstB[i]
        print(S, end=' ')
    print()