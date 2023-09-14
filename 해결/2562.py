# 최대값

from sys import stdin

mx = [0, 0]
for i in range(1, 10):
    n = int(stdin.readline())
    if mx[0] < n:
        mx = [n, i]

print(*mx, sep='\n')