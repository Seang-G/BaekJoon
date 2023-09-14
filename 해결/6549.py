# 히스토그램에서 가장 큰 직사각형
import time
from sys import stdin

S = list(map(int, stdin.readline().split()))

while S != [0]:
    start = time.time()
    N = S[0]
    S = S[1:]
    mx = 0
    stack_i = []
    stack_v = []

    for i, v in enumerate(S):
        ln = len(stack_i)
        if ln == 0:
            stack_i = [i]
            stack_v = [v]
            continue

        if stack_v[-1] < v:
            stack_v.append(v)
            stack_i.append(i)
            continue
        
        loc = -1
        for j in range(ln-1, -1, -1):
            if stack_v[j] < v:
                loc = j
                break

        for j in range(loc+1, ln):
            mx = max(mx, stack_v[j]*(i-stack_i[j]))

        ii = stack_i[loc+1]
        del stack_i[loc+1:]
        del stack_v[loc+1:]

        stack_i.append(ii)
        stack_v.append(v)
        
    for i in range(len(stack_i)):
        mx = max(mx, (N-stack_i[i]) * stack_v[i])

    print(mx)
    print(time.time()-start)
    S = list(map(int, stdin.readline().split()))