# 헌내기는 친구가 필요해

from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)

def move(poss):
  nextPoss = []

  for pos in poss:
  
    if pos[0] > 0 and campus[pos[0]-1][pos[1]] in ['O', 'P']:
      nextPoss.append((pos[0]-1, pos[1]))
      if campus[pos[0]-1][pos[1]] == 'P': answer[0] += 1
      campus[pos[0]-1][pos[1]] = "X"

    if pos[0] < N-1 and campus[pos[0]+1][pos[1]] in ['O', 'P']:
      nextPoss.append((pos[0]+1, pos[1]))
      if campus[pos[0]+1][pos[1]] == 'P': answer[0] += 1
      campus[pos[0]+1][pos[1]] = "X"

    if pos[1] > 0 and campus[pos[0]][pos[1]-1] in ['O', 'P']:
      nextPoss.append((pos[0], pos[1]-1))
      if campus[pos[0]][pos[1]-1] == 'P': answer[0] += 1
      campus[pos[0]][pos[1]-1] = "X"

    if pos[1] < M-1 and campus[pos[0]][pos[1]+1] in ['O', 'P']:
      nextPoss.append((pos[0], pos[1]+1))
      if campus[pos[0]][pos[1]+1] == 'P': answer[0] += 1
      campus[pos[0]][pos[1]+1] = "X"

  if nextPoss: move(list(nextPoss))

answer = [0]

N, M = map(int, input().split())
campus = []

for i in range(N):
  row = list(stdin.readline().strip())
  if "I" in row: I_pos = (i, row.index("I"))
  campus.append(row)

move([I_pos])

print(answer[0] if answer[0] > 0 else "TT")