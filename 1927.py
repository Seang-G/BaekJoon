import heapq
from sys import stdin

q = []
n = int(input())
for _ in range(n):
    x = int(stdin.readline())
    
    if x != 0: heapq.heappush(q, x)
    else:
        if q: print(heapq.heappop(q))
        else: print(0)