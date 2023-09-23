# 스티커

from sys import stdin

T = int(input())
for _ in range(T):
  n = int(input())
  stickers = [list(map(int, stdin.readline().split())), list(map(int, stdin.readline().split()))]
  
  for i in range(n):
    for j in range(2):
      if i > 0:
        cor = stickers[(j+1)%2][i-1]
        if i > 1:
          cor = max(stickers[(j+1)%2][i-1], stickers[(j+1)%2][i-2])
        stickers[j][i] += cor

  print(max(stickers[0][-1], stickers[1][-1]))