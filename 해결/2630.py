# 색종이 만들기

from sys import stdin

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, stdin.readline().split())))

def f(x, y, n):
    sm = 0
    for row in S[x:x+n]:
        sm += sum(row[y:y+n])
    if sm == 0: return [1, 0]
    if sm == n*n: return [0, 1]

    wb = f(x, y, n//2)
    wb_c = f(x+n//2, y, n//2)
    wb[0] += wb_c[0]
    wb[1] += wb_c[1]

    wb_c = f(x, y+n//2, n//2)
    wb[0] += wb_c[0]
    wb[1] += wb_c[1]

    wb_c = f(x+n//2, y+n//2, n//2)
    wb[0] += wb_c[0]
    wb[1] += wb_c[1]

    return wb

print(*f(0, 0, N), sep='\n')