# 소인수분해

from math import sqrt

che = list(range(2, 3164))
for n in che:
    for x in range(n*2, 3164, n):
        try: che.remove(x)
        except: continue

N = int(input())
i = 0
while N != 1:
    if che[i] > sqrt(N):
        print(N)
        break

    if N%che[i] == 0:
        print(che[i])
        N //= che[i]
    else: i += 1