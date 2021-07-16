# 베르트랑 공준

from math import sqrt

MAX = 123456*2+1

TF = [False, False] + [True]*(MAX-1)
for i in range(int(sqrt(MAX))+1):
    if TF[i]:
        for x in range(i*2, MAX+1, i):
            TF[x] = False

N = int(input())
while N != 0:
    print(TF[N+1:N*2+1].count(True))
    N = int(input())