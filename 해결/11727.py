# 2×n 타일링 2

n = int(input())

fibo = [1, 3, *[0 for i in range(2, 1000-2)]]

for i in range(2, 1000):
  fibo[i] = fibo[i-1] + fibo[i-2]*2

print(fibo[n-1]%10007)