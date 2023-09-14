# 전깃줄

import sys

N = int(input())
dic = {}

for _ in range(N):
    t = tuple(map(int, sys.stdin.readline().split()))
    dic[t] = 1

ks = sorted(list(dic.keys()))

for i, v in enumerate(ks):
    for u in ks[i+1:]:
        if (v[0] > u[0] and v[1] > u[1]) or (v[0] < u[0] and v[1] < u[1]):
            dic[u] = max(dic[v]+1, dic[u])

print(N - max(dic.values()))