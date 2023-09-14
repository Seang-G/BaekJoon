# 쿼드트리

from sys import stdin

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, list(stdin.readline().strip()))))

def f(x, y, n):
    sm = 0
    for row in S[x:x+n]:
        sm += sum(row[y:y+n])
    if sm == 0: return [0]
    if sm == n*n: return [1]

    return [(f(x, y, n//2)), (f(x, y+n//2, n//2)), (f(x+n//2, y, n//2)), (f(x+n//2, y+n//2, n//2))]

def prt(lst):
    if type(lst[0]) == type(1): print(lst[0], end='')
    else:
        print('(', end='')
        for n in lst:
            prt(n)
        print(')', end='')
    
prt(f(0, 0, N))