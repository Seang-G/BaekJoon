# 단어 정렬

import sys

N = int(input())
S = set([])
for _ in range(N):
    S.add(sys.stdin.readline().strip())

S = sorted(sorted(list(S)), key=len)
print(*S, sep='\n')