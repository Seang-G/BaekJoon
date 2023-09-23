# 이중 우선순위 큐

from sys import stdin
from collections import defaultdict
import heapq

T = int(input())
for _ in range(T):
  k = int(input())
  q1 = []
  q2 = []
  dic = defaultdict(int)
  
  IDcnt = 0
  for __ in range(k):
    oper, v = stdin.readline().strip().split()
    v = int(v)
    if oper == "I": 
      IDcnt += 1
      dic[v] += 1
      heapq.heappush(q1, v)
      heapq.heappush(q2, v*(-1))
    else:
      if IDcnt <= 0: continue
      if v == 1: 
        mx = heapq.heappop(q2)*(-1)
        while dic[mx] <= 0: mx = heapq.heappop(q2)*(-1)
        dic[mx] -= 1
      else: 
        mn = heapq.heappop(q1)
        while dic[mn] <= 0: mn = heapq.heappop(q1)
        dic[mn] -= 1
      IDcnt -= 1

  if IDcnt <= 0: print("EMPTY")
  else: 
    mx = heapq.heappop(q2)*(-1)
    mn = heapq.heappop(q1)

    while dic[mx] <= 0: mx = heapq.heappop(q2)*(-1)
    while dic[mn] <= 0: mn = heapq.heappop(q1)
    
    print(mx, mn)