def explore(pos, cnt):
  x, y = pos
  if x > 0 and zido[x-1][y]:
    zido[x-1][y] = 0
    cnt = explore((x-1, y), cnt+1)

  if x < N-1 and zido[x+1][y]:
    zido[x+1][y] = 0
    cnt = explore((x+1, y), cnt+1)

  if y > 0 and zido[x][y-1]:
    zido[x][y-1] = 0
    cnt = explore((x, y-1), cnt+1)

  if y < N-1 and zido[x][y+1]:
    zido[x][y+1] = 0
    cnt = explore((x, y+1), cnt+1)

  return cnt

N = int(input())
zido = [list(map(int, list(input()))) for _ in range(N)]

answer = []

for i in range(N):
  for j in range(N):
    if zido[i][j]:
      answer.append(explore((i, j), 0))

print(len(answer), *sorted(answer), sep="\n")