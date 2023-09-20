# 뱀과 사다리 게임

from sys import setrecursionlimit
setrecursionlimit(1000000)

def roll_dice(poss, depth):
  nxt_pos = set([])
  for pos in poss:
    if pos+6 >= 100: return depth
    
    for i in range(1, 7):
      if not gameboard[pos+i]:
        gameboard[pos+i] = depth
        if pos+i in ladders_T[0]:
          mov_pos = ladders_T[1][ladders_T[0].index(pos+i)]
          if not gameboard[mov_pos]:
            nxt_pos.add(mov_pos)
            gameboard[mov_pos] = depth
        elif pos+i in snakes_T[0]:
          mov_pos = snakes_T[1][snakes_T[0].index(pos+i)]
          if not gameboard[mov_pos]:
            nxt_pos.add(mov_pos)
            gameboard[mov_pos] = depth
        else:
          nxt_pos.add(pos+i)

  return roll_dice(list(nxt_pos), depth+1)

N, M = map(int, input().split())

ladders = [tuple(map(int, input().split())) for _ in range(N)]
snakes = [tuple(map(int, input().split())) for _ in range(M)]

ladders_T = list(zip(*ladders))
snakes_T = list(zip(*snakes))

gameboard = [0 for _ in range(101)]

print(roll_dice([1], 1))