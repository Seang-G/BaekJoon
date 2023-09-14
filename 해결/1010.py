# 다리 놓기

T = int(input())

f = [[0]*30] + [[i for i in range(30)]] + [[0]*30 for i in range(28)]

for i in range(2, 30):
    for j in range(1, 30):
        f[i][j] = f[i][j-1] + f[i-1][j]

for _ in range(T):
    N, M = map(int, input().split())
    print(f[N][M-N+1])
    