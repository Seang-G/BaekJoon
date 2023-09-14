# 물병

N, K = map(int, input().split())

n = 1
while n<N: n *= 2

while K > 1:
  N -= n//2
  n = 1
  while n<N: n *= 2
  K -= 1

print(n-N)