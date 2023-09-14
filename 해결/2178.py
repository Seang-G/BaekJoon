# 미로 탐색

from sys import setrecursionlimit

setrecursionlimit(1000000)

def tamsec(poss, depth):
  if (N-1, M-1) in poss: return depth

  next_poss = []
  for pos in poss:
    moveables = []

    if pos[0] > 0 and miro[pos[0]-1][pos[1]] == "1":
      next_poss.append((pos[0]-1, pos[1]))
      miro[pos[0]-1][pos[1]] = "0"

    if pos[0] < N-1 and miro[pos[0]+1][pos[1]] == "1":
      next_poss.append((pos[0]+1, pos[1]))
      miro[pos[0]+1][pos[1]] = "0"

    if pos[1] > 0 and miro[pos[0]][pos[1]-1] == "1":
      next_poss.append((pos[0], pos[1]-1))
      miro[pos[0]][pos[1]-1] = "0"

    if pos[1] < M-1 and miro[pos[0]][pos[1]+1] == "1":
      next_poss.append((pos[0], pos[1]+1))
      miro[pos[0]][pos[1]+1] = "0"

  return tamsec(next_poss, depth+1)

N, M = map(int, input().split())
miro = [list(input()) for _ in range(N)]

print(tamsec([(0, 0)], 1))