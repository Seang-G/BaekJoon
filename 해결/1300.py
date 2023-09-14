# K번째 수

import time


N = int(input())
k = int(input())
start = time.time()

s = 1
e = N*N
mid = (s+e)//2

while s < e:
    mid = (s+e)//2

    c = 0
    d = 0
    for i in range(1, N+1):
        d += min((mid-1)//i, N)
        c += min(mid//i, N)
        if d >= k:
            e = mid-1
            break
    else:
        if k <= c:
            s = mid
            break
        s = mid+1

print(s)

print(time.time() - start)