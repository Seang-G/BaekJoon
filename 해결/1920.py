# 수 찾기

from bisect import bisect_left as bl

N = int(input())
NN = list(map(int, input().split())) + [2**31]
M = int(input())
MM = list(map(int, input().split()))
NN.sort()

for n in MM:
    print(1 if n == NN[bl(NN, n)] else 0)