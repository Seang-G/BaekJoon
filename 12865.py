# 평범한 배낭

import sys

N, K = map(int, input().split())

S = []
for i in range(N):
    S.append(tuple(map(int, sys.stdin.readline().split())))

S.sort(key=lambda x: x[1], reverse=True)
S.sort(key=lambda x: x[0])

dp = [[0, []] for _ in range(K+1)]

for i, v in enumerate(S):
    if v[0] <= K and dp[v[0]][0] == 0:
        dp[v[0]] = [v[1], [i]]

for i in range(N):
    for j in range(1, K+1-S[i][0]):
        if dp[j][0] !=0 and i not in dp[j][1]:
            a = S[i][0] + j
            if dp[a][0] < S[i][1] + dp[j][0]:
                dp[a][0] =  S[i][1] + dp[j][0]
                dp[a][1] = [i] + dp[j][1]

print(max(list(zip(*dp))[0]))