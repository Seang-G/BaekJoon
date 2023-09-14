# 포도주 시식

import sys

N = int(input())
S = []

for _ in range(N):
    n = int(sys.stdin.readline())
    S.append([n, n, n])

for i in range(N-1):
    if S[i][0] == S[i][1]: S[i+1][1] += max(S[i])
    else: S[i+1][1] += max(S[i][0], S[i][2])

    if i != N-2:
        S[i+2][2] = max(S[i+2][2], S[i+2][0] + max(S[i]))

    if i < N-3:
        S[i+3][2] = max(S[i+3][2], S[i+3][0] + max(S[i]))

print(max(S[N-1]+S[N-2]))