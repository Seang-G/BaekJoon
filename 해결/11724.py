# 연결 요소의 개수

from sys import stdin, setrecursionlimit
setrecursionlimit(100000)

def search(connected_vortexes):
  for connected_vortex in connected_vortexes:
    if not visited[connected_vortex]:
      visited[connected_vortex] = True
      search(dic[connected_vortex])

N, M = map(int, input().split())

dic = {i:[] for i in range(1, N+1)}
visited = [False for _ in range(N+1)]

for _ in range(M):
  u, v = map(int, stdin.readline().strip().split())
  dic[u].append(v)
  dic[v].append(u)

answer = 0
while False in visited[1:]:
  answer += 1
  start = visited[1:].index(False)+1
  visited[start] = True
  search(dic[start])

print(answer)