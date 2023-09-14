# 나이순 정렬

import sys

N = int(input())
S = []
for _ in range(N):
    S.append(sys.stdin.readline().split())

S = sorted(S, key=lambda x: int(x[0]))
for l in S: print(l[0], l[1])