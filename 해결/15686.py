# 치킨 배달

from itertools import combinations as cb

def calc_dist(chickens):
  dists = [3000 for _ in range(len(houses))]
  for i, house in enumerate(houses):
    for chicken in chickens:
      dists[i] = min(dists[i], abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))

  return sum(dists)

N, M = map(int, input().split())
city = []
chickens = []
houses = []

for i in range(N):
  for j, kan in enumerate(map(int, input().split())):
    if kan == 1: houses.append((i, j))
    elif kan == 2: chickens.append((i, j))

answer = 50*2*13
for selected in cb(chickens, M):
  answer = min(answer, calc_dist(selected))

print(answer)