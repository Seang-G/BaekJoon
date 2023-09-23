# 구간 합 구하기 5

from sys import stdin

N, M = map(int, input().split())
table = [list(map(int, stdin.readline().split())) for _ in range(N)]

sum_table = []
for i in range(N):
  sum_table.append([0, table[i][0]])
  for j in range(2, N+1):
    sum_table[i].append(sum_table[i][j-1]+table[i][j-1])
    
for _ in range(M):
  x1, y1, x2, y2 = map(int, stdin.readline().split())
  print(sum([row[y2]-row[y1-1] for row in sum_table[x1-1:x2]]))