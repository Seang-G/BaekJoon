# RGB거리

import sys

N = int(input())

r, g, b = 0, 0, 0

for i in range(N):
    R, G, B = map(int, sys.stdin.readline().split())
    R, G, B = R+min(g, b), G+min(r, b), B+min(r, g)
    r, g, b = R, G, B

print(min([r, g, b]))