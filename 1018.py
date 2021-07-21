# 체스판 다시 칠하기

N, M = map(int, input().split())

board = [['W' if (i+j)%2==0 else 'B' for i in range(M)] for j in range(N)]
diff = 0


for i in range(N):
    line = list(input())
    for j in range(M):
        if line[j] == board[i][j]: board[i][j] = False
        else: board[i][j] = True

mn = 32
for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for line in board[i:i+8]:
            cnt += line[j:j+8].count(True)
        mn = min([mn, cnt, 64-cnt])

print(mn)