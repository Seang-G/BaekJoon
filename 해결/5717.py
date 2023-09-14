# 상근이의 친구들

from sys import stdin

A, B = map(int, input().split())
while A != 0 or B != 0:
    print(A+B)
    A, B = map(int, input().split())