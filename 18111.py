# 마인크래프트

# 시간초과로 PyPy 사용

N, M, B = map(int, input().split())
site = [list(map(int, input().split())) for _ in range(N)]

answer = [1000000000, 0]
for hight in range(257):
  need = 0
  needless = 0

  # site[i][j] 로 접근하는 것 보다 이 방법이 빠르다.
  for row in site:
    for pixel in row:
      if hight > pixel:
        need += hight - pixel
      else:
        needless += pixel - hight

  if needless+B < need: break
  if answer[0] >= need + needless*2:
    answer = [need + needless*2, hight]

print(*answer)