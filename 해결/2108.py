# 통계학

import sys

Max = 8001
N = int(input())

S = [0] * (Max+1)
Avg = 0
Mid = [0, True]
Com = [0, True]
Ran = [4001, -4001]

for _ in range(N):
    n = int(sys.stdin.readline())
    Avg += n
    Ran[0] = min(Ran[0], n)
    Ran[1] = max(Ran[1], n)
    S[n + Max//2 + 1] += 1

cnt = 0
for i in range(Max+1):
    if S[i] != 0:
        cnt += S[i]
        if cnt >= N//2+1 and Mid[1]: Mid = [i - Max//2 - 1, False]
        if S[Com[0]] < S[i]: Com = [i, True]
        elif S[Com[0]] == S[i] and Com[1]: Com = [i, False]

Avg = round(Avg/N)
Mid = Mid[0]
Com = Com[0] - Max//2 - 1
Ran = Ran[1] - Ran[0]

print(Avg, Mid, Com, Ran, sep='\n')