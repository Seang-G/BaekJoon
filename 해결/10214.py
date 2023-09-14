# Baseball

from sys import stdin

T = int(input())
for _ in range(T):
    Y = 0
    K = 0
    for i in range(9):
        a, b = map(int, stdin.readline().split())
        Y += a
        K += b
    if Y > K: print('Yonsei')
    elif Y < K: print('Korea')
    else: print('Draw')