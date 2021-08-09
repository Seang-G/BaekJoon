# 행렬 제곱

from sys import stdin

p = 1000
N, M = map(int, input().split())
Q = []

for _ in range(N):
    Q.append(list(map(lambda x: int(x)%p, stdin.readline().split())))

def mul(A, B):
    lst = []
    for lstA in A:
        lst.append([])
        for lstB in B:
            S = 0
            for i in range(N):
                S += lstA[i] * lstB[i]
                S %= p
            lst[-1].append(S)
    return lst

def f(b):
    if b==1: return Q
    else:
        G = f(b//2)
        lst = mul(G, list(zip(*G)))
        if b%2==1: lst = mul(lst, list(zip(*Q)))

        return lst

for n in f(M):
    print(*n)