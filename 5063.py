# TGN

from sys import stdin

N = int(input())

for _ in range(N):
    r, e, c = map(int, stdin.readline().split())
    if r > e-c: print('do not advertise')
    elif r < e-c: print('advertise')
    else: print('does not matter')