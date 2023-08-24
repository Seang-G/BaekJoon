# 마인크래프트

N, M, B = map(int, input().split())
site = [list(map(int, input().split())) for _ in range(N)]

avg = round(sum(map(lambda x: sum(x)/M, site))/N)

answer = [100000, 0]
for hight in [max(0, avg-2), max(0, avg-1), avg, avg+1, avg+2]:
  need = 0
  needless = 0

  for i in range(N):
    for j in range(M):
      if hight > site[i][j]:
        need += hight - site[i][j]
      else:
        needless += site[i][j] - hight

  if needless-need > B: continue
  if answer[0] > need + needless*2:
    answer = [need + needless*2, hight]

print(*answer)