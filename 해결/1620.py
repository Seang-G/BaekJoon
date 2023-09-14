# 나는야 포켓몬 마스터 이다솜

from sys import stdin

N, M = map(int, input().split())

dogam = {}
for number in range(1, N+1):
  pokemon = stdin.readline().strip()
  dogam[str(number)] = pokemon
  dogam[pokemon] = str(number)

for _ in range(M):
  print(dogam[stdin.readline().strip()])