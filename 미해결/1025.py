# 제곱수 찾기

def check(n):
  
  if n**0.5 - int(n**0.5) == 0: return True
  return False

N, M = map(int, input().split())
table = [input() for _ in range(N)]
answer = -1

for N_inc in [i for i in range(1-N, N) if i != 0]:
  for M_inc in [i for i in range(1-M, M) if i != 0]:
    
    n = "0"
    i = j = 0
    while i < N and j < M:
      n += table[i][j]
    print(n)
    if check(int(n)): answer = max(answer, int(n))

print(answer)