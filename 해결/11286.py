# 절댓값 힙

import heapq
from sys import stdin

N = int(input())

q = []
for _ in range(N):
    x = int(stdin.readline())
    if x == 0:
        if q: print(heapq.heappop(q)[1])
        else: print(0)
    else:
        x_lst = [abs(x), x]
        heapq.heappush(q, x_lst)