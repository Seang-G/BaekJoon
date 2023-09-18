# 카잉달력

from sys import stdin

for _ in range(int(input())):

  answer = 0
  M, N, x, y = map(int, stdin.readline().strip().split())

  while x != y:
    if answer > M*N:
      answer = -1
      break

    if x < y: 
      answer += x
      y -= x
      x = M

    else:
      answer += y
      x -= y
      y = N
      
  print(answer if answer == -1 else answer+x)