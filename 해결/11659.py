# 구간 합 구하기 4

from sys import stdin

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

sums = [numbers[0]]
for i in range(1, N):
  sums.append(sums[i-1] + numbers[i])

for _ in range(M):
  i, j = map(int, stdin.readline().strip().split())
  if i<2: print(sums[j-1])
  else: print(sums[j-1] - sums[i-2])