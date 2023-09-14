# 스도쿠

board = [list(map(int, input().split())) for _ in range(9)]
row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
box = [[False] * 10 for _ in range(9)]
a, z = [0]*81, 0

def sdk(idx=0):
    if idx == z:
        for line in board:
            print(' '.join(map(str, line)))
        exit(0)
    x, y = a[idx]//9, a[idx]%9

    for i in range(1, 10):
        if not (row[x][i] or col[y][i] or box[x//3*3+y//3][i]):
            row[x][i] = col[y][i] = box[x//3*3+y//3][i] = True
            board[x][y] = i
            sdk(idx+1)
            row[x][i] = col[y][i] = box[x//3*3+y//3][i] = False
            board[x][y] = 0

for i in range(9):
    for j in range(9):
        n = board[i][j]
        if n:
            row[i][n] = True
            col[j][n] = True
            box[i//3*3+j//3][n] = True
        else:
            a[z] += i*9 + j
            z += 1

sdk()