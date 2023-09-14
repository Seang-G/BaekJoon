# 소수 구하기

from math import sqrt
M, N = map(int, input().split())

TF = [False, False] + [True]*(N-1)
for i in range(int(sqrt(N))+1):
    if TF[i]:
        for x in range(i*2, N+1, i):
            TF[x] = False

for i in range(M, N+1):
    if TF[i]: print(i)