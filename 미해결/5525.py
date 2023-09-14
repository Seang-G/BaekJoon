# IOIOI

import re

answer = 0

N = int(input())
M = int(input())
S = input()

cnt = 0
I_turn = True
for c in S:
  print(c, cnt)
  if I_turn:
    if c == "I":
      cnt += 1
      I_turn = False
    else: 
      answer += max(0, (cnt)/2-N)
      cnt = 0
  else:
    if c == "O":
      cnt += 1
      I_turn = True
    else:
      answer += max(0, (cnt-1)/2-N)
      cnt = 1
    

print(answer)