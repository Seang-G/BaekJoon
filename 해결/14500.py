# 테트로미노

from sys import stdin

cases = {(2, 0): [(3, 0), (2, 1), (2, -1), (1, -1), (0, 1), (1, 1)], (1, 1): [(1, 2), (2, 1), (0, 1)], (1, -1): [(2, -1)]}

N, M = map(int, input().split())
paper = [list(map(int, stdin.readline().split())) for _ in range(N)]

ans = 0

for i in range(N):
  for j in range(M):
    try: temp1 = paper[i][j]+paper[i+1][j]
    except: pass
    for pos1 in cases.keys():
      try:
        x, y = pos1
        temp2 = paper[i+x][j+y]
      except: continue
      for pos2 in cases[pos1]:
          try: ans = max(ans, temp1+temp2+paper[i+pos2[0]][j+pos2[1]])
          except: continue

    try: temp1 = paper[i][j]+paper[i][j+1]
    except: pass
    for pos1 in cases.keys():
      try:
        y, x = pos1
        temp2 = paper[i+x][j+y]
      except: continue
      for pos2 in cases[pos1]:
          try: ans = max(ans, temp1+temp2+paper[i+pos2[1]][j+pos2[0]])
          except: continue

print(ans)