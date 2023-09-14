# 공유기 설치

from sys import stdin

N, C = map(int, input().split())
x = [int(stdin.readline()) for _ in range(N)]
x.sort()

s = x[1] - x[0]
e = x[N-1] - x[0]
c = 2
ans = e-s

while s <= e:
    c = 1
    mid = (s+e)//2
    sp = x[0]

    for g in x[1:]:
        if g-sp >= mid:
            sp = g
            c += 1
    
    if c >= C:
        s = mid+1
        ans = mid
    else: e = mid-1

print(ans)