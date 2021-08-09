# 종이의 개수

from sys import stdin

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, stdin.readline().split())))

def f(x, y, n):
    m = z = o = 0
    sm = 0
    a = S[x][y]
    for row in S[x:x+n]:
        if n != row[y:y+n].count(a): break
    else:
        if a == -1: return [1, 0, 0]
        elif a == 0: return [0, 1, 0]
        elif a == 1: return [0, 0, 1]

    wb = [0, 0, 0]

    for i in [x, x+n//3, x+(n//3)*2]:
        for j in [y, y+n//3, y+(n//3)*2]:
            wb_c = f(i, j, n//3)
            for z in range(3):
                wb[z] += wb_c[z]

    return wb

print(*f(0, 0, N), sep='\n')