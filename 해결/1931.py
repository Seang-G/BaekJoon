# 회의실 배정

import sys

N = int(input())

A = []
for _ in range(N):
    A.append(tuple(map(int, sys.stdin.readline().split())))

A.sort(key=lambda x: x[0])
A.sort(key=lambda x: x[1])

ans = 0
e = 0
for i in range(N):
    if e <= A[i][0]:
        ans += 1
        e = A[i][1]

print(ans)