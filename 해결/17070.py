#파이프 옮기기 1

from sys import setrecursionlimit

setrecursionlimit(1000000)

def move_hor(pos):
  if pos[1] < N-1 and house[pos[0]][pos[1]+1] != 1:
    if (pos[0], pos[1]+1) in dic["hor"]:
      dic["hor"][(pos[0], pos[1]+1)] += dic["hor"][pos]
    else:
      dic["hor"][(pos[0], pos[1]+1)] = dic["hor"][pos]

  if pos[1] < N-1 and pos[0] < N-1 and 1 not in [house[pos[0]][pos[1]+1], house[pos[0]+1][pos[1]], house[pos[0]+1][pos[1]+1]]:
    if (pos[0]+1, pos[1]+1) in dic["diag"]:
      dic["diag"][(pos[0]+1, pos[1]+1)] += dic["hor"][pos]
    else:
      dic["diag"][(pos[0]+1, pos[1]+1)] = dic["hor"][pos]

def move_ver(pos):
  if pos[0] < N-1 and house[pos[0]+1][pos[1]] != 1:
    if (pos[0]+1, pos[1]) in dic["ver"]:
      dic["ver"][(pos[0]+1, pos[1])] += dic["ver"][pos]
    else:
      dic["ver"][(pos[0]+1, pos[1])] = dic["ver"][pos]

  if pos[0] < N-1 and pos[1] < N-1 and 1 not in [house[pos[0]][pos[1]+1], house[pos[0]+1][pos[1]], house[pos[0]+1][pos[1]+1]]:
    if (pos[0]+1, pos[1]+1) in dic["diag"]:
      dic["diag"][(pos[0]+1, pos[1]+1)] += dic["ver"][pos]
    else:
      dic["diag"][(pos[0]+1, pos[1]+1)] = dic["ver"][pos]


def move_diag(pos):
  if pos[0] < N-1 and house[pos[0]+1][pos[1]] != 1:
    if (pos[0]+1, pos[1]) in dic["ver"]:
      dic["ver"][(pos[0]+1, pos[1])] += dic["diag"][pos]
    else:
      dic["ver"][(pos[0]+1, pos[1])] = dic["diag"][pos]

  if pos[1] < N-1 and house[pos[0]][pos[1]+1] != 1:
    if (pos[0], pos[1]+1) in dic["hor"]:
      dic["hor"][(pos[0], pos[1]+1)] += dic["diag"][pos]
    else:
      dic["hor"][(pos[0], pos[1]+1)] = dic["diag"][pos]

  if pos[0] < N-1 and pos[1] < N-1 and 1 not in [house[pos[0]][pos[1]+1], house[pos[0]+1][pos[1]], house[pos[0]+1][pos[1]+1]]:
    if (pos[0]+1, pos[1]+1) in dic["diag"]:
      dic["diag"][(pos[0]+1, pos[1]+1)] += dic["diag"][pos]
    else:
      dic["diag"][(pos[0]+1, pos[1]+1)] = dic["diag"][pos]


def move():
  poss_hor = list(dic["hor"].keys())
  poss_ver = list(dic["ver"].keys())
  poss_diag = list(dic["diag"].keys())
  if not poss_hor+poss_ver+poss_diag: return

  for pos in poss_hor:
    if pos == (N-1, N-1): answer[0] += dic["hor"][pos]
    move_hor(pos)
    dic["hor"].pop(pos)

  for pos in poss_ver:
    if pos == (N-1, N-1): answer[0] += dic["ver"][pos]
    move_ver(pos)
    dic["ver"].pop(pos)

  for pos in poss_diag:
    if pos == (N-1, N-1): answer[0] += dic["diag"][pos]
    move_diag(pos)
    dic["diag"].pop(pos)

  move()

N = int(input())
house =[list(map(int, input().split())) for _ in range(N)]
dic = {"hor":{(0, 1):1}, "ver":{}, "diag":{}}

answer = [0]

move()

print(answer[0])