# 어린 왕자

from sys import stdin

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    cnt = 0
    n = int(input())
    for __ in range(n):
        cx, cy, r = map(int, stdin.readline().split())
        if ((x1-cx)**2 + (y1-cy)**2 < r**2) != ((x2-cx)**2 + (y2-cy)**2 < r**2):
            cnt += 1
    print(cnt)