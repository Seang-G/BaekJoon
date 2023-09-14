# 2xN 타일링

N = int(input())

fibo = [[0 for _ in range(1001)], [i for i in range(1001)]]

for i in range(2, 501):
  fibo.append([])
  for j in range(1001-i):
    if j < i: fibo[i].append(0)
    else: fibo[i].append(fibo[i][j-1]+fibo[i-1][j-1])
    
answer = 1
i = 1
while N/2 >= i:
  answer += fibo[i][N-i]
  answer %= 10007
  i += 1

print(answer)