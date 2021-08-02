# 쉬운 계단 수

N = int(input())

S = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] + [[0]*10 for _ in range(N-1)]

for i in range(1, N):
    S[i][0] = S[i-1][1]
    for j in range(1, 9):
        S[i][j] = S[i-1][j-1] + S[i-1][j+1]
    S[i][9] = S[i-1][8]

print(sum(S[N-1][1:])%1000000000)