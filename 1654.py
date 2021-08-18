# 랜선 자르기

from sys import stdin

K, N = map(int, input().split())
lan = []
for _ in range(K):
    lan.append(int(stdin.readline()))

def bi(s, e):
    if e-s == 1 or e == s:
        return e if sum(map(lambda x: x//e, lan)) >= N else s
    mid = (s+e)//2
    S = sum(map(lambda x: x//mid, lan))
    if S < N: return bi(s, mid)
    else: return bi(mid, e)

print(bi(1, max(lan)))