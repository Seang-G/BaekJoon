# 행렬

import sys
# 백준의 재귀 깊이는 1000으로 제한되어 있음
# => 재귀를 없애거나 늘리는 방식 사용
sys.setrecursionlimit(3000)

def solve():
  if A == B: return 0
  if N < 3 or M < 3: return -1

  ans = search(A.copy(), 0)
  return ans

# 3x3 부분행렬에 대해 0은 1로, 1은 0으로 바꾸는 함수
# 리스트는 함수 내에서 바꿔도 밖까지 적용이 됨
def change(lst, row, col):
  for i in range(row, row+3):
    for j in range(col, col+3):
      lst[i][j] = (lst[i][j]+1)%2

# 리스트를 복제할 때는 .copy() 활용
def search(A_clone, dep):
  if A_clone == B: return dep

  for i in range(N-2):
    for j in range(M-2):
      if A_clone[i][j] != B[i][j]:
        A_plane = A_clone.copy()
        change(A_clone, i, j)

        answer = search(A_clone.copy(), dep+1)
        if answer != -1: return answer
        A_clone = A_plane.copy()
  
  return -1

N, M = map(int, input().split())

A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]

print(solve())