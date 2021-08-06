# 프린터 큐

import heapq
from sys import stdin

T = int(input())

for _ in range(T):
    N, M = map(int, stdin.readline().split())
    Q = list(map(int, stdin.readline().split()))
    H = []

    for n in Q: heapq.heappush(H, 10-n)

    cnt = 1
    while True:
        mx = 10 - heapq.heappop(H)

        idx = Q.index(mx)
        if idx == M:
            print(cnt)
            break
        Q = Q[idx+1:] + Q[:idx]
        if M > idx: M -= (idx+1)
        else: M -= idx
        if M < 0: M += len(Q)
        
        cnt += 1