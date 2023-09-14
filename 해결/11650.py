# 좌표 정렬하기

import sys

N = int(input())
S = []
for _ in range(N):
    S.append(tuple(map(int, sys.stdin.readline().split())))
S = sorted(sorted(S, key=lambda x: x[1]))

for p in S:
    print(p[0], p[1], sep=' ')