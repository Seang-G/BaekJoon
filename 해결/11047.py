# 동전 0

import sys

N, K = map(int, input().split())

A = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n <= K: A.append(n)
    else: N -= 1

ans = 0
for i in range(N-1, -1, -1):
    ans += K//A[i]
    K %= A[i]

print(ans)