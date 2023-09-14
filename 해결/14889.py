# 스타트와 링크

import sys
import math

N = int(input())
S_ = []
for _ in range(N): S_.append(list(map(int, sys.stdin.readline().split())))
S = [[S_[i][j]+S_[j][i] for j in range(N)] for i in range(N)]
MN = math.inf

def ST(start, link, ss, ls, i):
    if len(start) == N//2:
        for n in range(i, N):
            for m in link:
                ls += S[n][m]
            link += [n]
        LK(ss, ls)
        del link[-N+i:]
        

    elif len(link) == N//2:
        for n in range(i, N):
            for m in start:
                ss += S[n][m]
            start.append(n)
        LK(ss, ls)
        del start[-N+i:]

    else:
        temp = 0
        for n in start: temp += S[i][n]
        ST(start+[i], link, ss+temp, ls, i+1)

        temp = 0
        for n in link: temp += S[i][n]
        ST(start, link+[i], ss, ls+temp, i+1)
    
def LK(ss, ls):
    global MN
    
    MN = min(MN, abs(ss - ls))

ST([0], [], 0, 0, 1)

print(MN)