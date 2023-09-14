# 계단 오르기

import sys

T = int(input())
S = []

for _ in range(T):
    n = int(sys.stdin.readline())
    S.append([n, n, n])

for i in range(T-1):
    if S[i][0] == S[i][1]: S[i+1][1] += max(S[i])
    else: S[i+1][1] += max(S[i][0], S[i][2])
    if i == T-2: break
    S[i+2][2] += max(S[i])

print(max(S[-1]))