# 쉬운 최단거리

from sys import stdin

def BFS(nows, depth=0):
  next_step = set([])
  for now in nows:
    if mapp[now[0]][now[1]] == 0 or answer[now[0]][now[1]] != 0: continue
    answer[now[0]][now[1]] = depth
    if now[0] > 0: next_step.add((now[0]-1, now[1])) 
    if now[0] < n-1: next_step.add((now[0]+1, now[1])) 
    if now[1] > 0: next_step.add((now[0], now[1]-1)) 
    if now[1] < m-1: next_step.add((now[0], now[1]+1)) 

  if nows: BFS(list(next_step), depth+1)
    

n, m = map(int, input().split())

mapp = []
answer = [[0 for _ in range(m)] for __ in range(n)]

for i in range(n):
  row = list(map(int, stdin.readline().strip().split()))
  if 2 in row: goal = (i, row.index(2))
  mapp.append(row)

BFS([goal])

for i in range(n):
  for j in range(m):
    if mapp[i][j] != 0 and answer[i][j] == 0: answer[i][j] = -1

answer[goal[0]][goal[1]] = 0
print(*map(lambda row: " ".join(map(str, row)), answer), sep="\n")