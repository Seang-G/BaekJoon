# 골드바흐의 추측

from math import sqrt

MAX = 10000

TF = [False, False] + [True]*(MAX-1)
for i in range(int(sqrt(MAX))+1):
    if TF[i]:
        for x in range(i*2, MAX+1, i):
            TF[x] = False

for _ in range(int(input())):
    N = int(input())
    
    for i in range(N//2+1, 1, -1):
        if TF[i] and TF[N-i]:
            print(min(N-i, i), max(i, N-i))
            break