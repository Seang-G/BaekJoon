# 적록색약

from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)

def tamsec(poss, color):
  if not poss: return
  nxt_poss = set([])
  for pos in poss:
    x, y = pos
    if x > 0 and pic[x-1][y] == color and not checked[x-1][y]:
      checked[x-1][y] = 1
      nxt_poss.add((x-1, y))
    if x < N-1 and pic[x+1][y] == color and not checked[x+1][y]:
      checked[x+1][y] = 1
      nxt_poss.add((x+1, y))
    if y > 0 and pic[x][y-1] == color and not checked[x][y-1]:
      checked[x][y-1] = 1
      nxt_poss.add((x, y-1))
    if y < N-1 and pic[x][y+1] == color and not checked[x][y+1]:
      checked[x][y+1] = 1
      nxt_poss.add((x, y+1))

  tamsec(list(nxt_poss), color)


N = int(input())

pic = [list(stdin.readline().strip()) for _ in range(N)]
checked = [[False for _ in range(N)] for __ in range(N)]
ans1 = 0
for i in range(N):
  for j in range(N):
    if not checked[i][j]:
      ans1 += 1
      tamsec([(i, j)], pic[i][j])


pic = list(map(lambda x: list("".join(x).replace("R", "G")), pic))
checked = [[False for _ in range(N)] for __ in range(N)]
ans2 = 0

for i in range(N):
  for j in range(N):
    if not checked[i][j]:
      ans2 += 1
      tamsec([(i, j)], pic[i][j])

print(ans1, ans2)