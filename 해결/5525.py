# IOIOI

answer = 0

N = int(input())
M = int(input())
S = input()

cnt = 0
I_turn = True
for c in S:
  if I_turn:
    if c == "I":
      cnt += 1
      I_turn = False
    else: 
      answer += int(max(0, (cnt)/2-N))
      cnt = 0
  else:
    if c == "O":
      cnt += 1
      I_turn = True
    else:
      answer += int(max(0, (cnt+1)/2-N))
      cnt = 1
    
answer += int(max(0, (cnt+1)/2-N))
print(int(answer))