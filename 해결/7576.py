# 토마토

from sys import stdin, setrecursionlimit

setrecursionlimit(10000000)

def bfs(tomatoes, depth=0):
  if not tomatoes: return depth-1

  for i, j in tomatoes:
    box[i][j] = 1

  next_tomatoes = set([])
  for i, j in tomatoes:
    if i > 0 and box[i-1][j] == 0: next_tomatoes.add((i-1,j))
    if i < N-1 and box[i+1][j] == 0: next_tomatoes.add((i+1,j))
    if j > 0 and box[i][j-1] == 0: next_tomatoes.add((i,j-1))
    if j < M-1 and box[i][j+1] == 0: next_tomatoes.add((i,j+1))

  return bfs(list(next_tomatoes), depth+1)

def is_all_ripe():
  for row in box:
    if 0 in row: return False
  return True

M, N = map(int, input().split())
box = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]

first = []

for i, row in enumerate(box):
  for j, tomato in enumerate(row):
    if tomato == 1:
      first.append((i, j))

answer = bfs(first)

if is_all_ripe(): print(answer)
else: print(-1)