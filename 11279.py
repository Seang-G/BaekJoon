import heapq
from sys import stdin

q = []
n = int(input())
for _ in range(n):
    x = int(stdin.readline())
    x = 100000 - x
    
    if x != 100000: heapq.heappush(q, x)
    else:
        if q: print(100000 - heapq.heappop(q))
        else: print(0)