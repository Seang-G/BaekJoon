# 내려가기

from sys import stdin
  
N = int(input())

board_mn = list(map(int, stdin.readline().split()))
board_mx = board_mn.copy()
for _ in range(N-1):
  n1, n2, n3 = map(int, stdin.readline().split())
  board_mn = (n1+min(board_mn[0], board_mn[1]), n2+min(board_mn[0], board_mn[1], board_mn[2]), n3+min(board_mn[1], board_mn[2]))
  board_mx = (n1+max(board_mx[0], board_mx[1]), n2+max(board_mx[0], board_mx[1], board_mx[2]), n3+max(board_mx[1], board_mx[2]))
  
print(max(board_mx), min(board_mn))