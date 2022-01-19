# 유기농 배추

from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y):
    if x >= len(memo) or x < 0: return False
    if y >= len(memo[0]) or y < 0: return False
    return True

def DFS(x, y):
    memo[x][y] = False
    for i in range(4):
        if check(x+dx[i], y+dy[i]) and memo[x+dx[i]][y+dy[i]]: DFS(x+dx[i], y+dy[i])

T = int(input())
for _ in range(T):
    cnt = 0
    x, y, n = map(int, input().split())
    memo = [[False for ___ in range(y)] for __ in range(x)]

    for __ in range(n):
        xx, yy = map(int, stdin.readline().split())
        memo[xx][yy] = True
    
    for i in range(x):
        for j in range(y):
            if memo[i][j]:
                cnt += 1
                DFS(i, j)
    print(cnt)