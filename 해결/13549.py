# 숨바꼭질 3

from sys import setrecursionlimit

setrecursionlimit(1000000)

def search(poss, depth):
  nxt = set([])
  for pos in poss:
    visited[pos] = True
    if pos == 0:
      if pos == K: return depth
      if not visited[1]: nxt.add(1)
      continue
    while pos<100002:
      if pos == K: return depth
      if not visited[pos+1]: nxt.add(pos+1)
      if not visited[pos-1]: nxt.add(pos-1)
      pos *= 2
  return search(list(nxt), depth+1)

N, K = map(int, input().split())
visited = [False for _ in range(100003)]

if N>=K: print(N-K)
else: print(search([N], 0))