# 토마토

from sys import stdin, setrecursionlimit
from itertools import chain

setrecursionlimit(100000000)

def ripe(ripeds, depth):
  if not ripeds: return depth

  nxt = set([])
  for riped in ripeds:
    x, y, z = riped

    if x > 0 and box[x-1][y][z]==0:
      nxt.add((x-1, y, z))
      box[x-1][y][z] = 1
    if x < H-1 and box[x+1][y][z]==0:
      nxt.add((x+1, y, z))
      box[x+1][y][z] = 1

    if y > 0 and box[x][y-1][z]==0:
      nxt.add((x, y-1, z))
      box[x][y-1][z] = 1
    if y < N-1 and box[x][y+1][z]==0:
      nxt.add((x, y+1, z))
      box[x][y+1][z] = 1

    if z > 0 and box[x][y][z-1]==0:
      nxt.add((x, y, z-1))
      box[x][y][z-1] = 1
    if z < M-1 and box[x][y][z+1]==0:
      nxt.add((x, y, z+1))
      box[x][y][z+1] = 1
  return ripe(nxt, depth+1)

M, N, H = map(int, input().split())
box = [[list(map(int, stdin.readline().strip().split())) for __ in range(N)] for _ in range(H)]

answer = ripe([(i, j, k) for k in range(M) for j in range(N) for i in range(H) if box[i][j][k] == 1], 0)

if 0 in chain(*chain(*box)): print(-1)
else: print(answer-1)