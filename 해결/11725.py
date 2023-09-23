# 트리의 부모 찾기

from sys import stdin, setrecursionlimit
from collections import defaultdict

setrecursionlimit(1000000)

def dfs(node):
  visited[node] = True
  children = tree[node]
  for child in children:
    if visited[child]: continue
    parent[child] = node
    dfs(child)

N = int(input())

tree = defaultdict(list)
parent = defaultdict(int)
visited = [False for _ in range(N+1)]

for _ in range(N-1):
  node1, node2 = map(int, stdin.readline().split())
  tree[node1].append(node2)
  tree[node2].append(node1)

dfs(1)

for i in range(2, N+1):
  print(parent[i])