# 나무 자르기

import bisect

N, M = map(int, input().split())
namu = list(map(int, input().split()))
namu.sort()

def bi(s, e):
    if e-s == 1 or e == s:
        lb = bisect.bisect_right(namu, e)
        return e if sum(namu[lb:])-(N-lb)*e >= M else s
    mid = (s+e)//2
    lb = bisect.bisect_right(namu, mid)
    S = sum(namu[lb:]) - (N-lb)*mid
    if S < M: return bi(s, mid)
    else: return bi(mid, e)

print(bi(0, namu[-1]))