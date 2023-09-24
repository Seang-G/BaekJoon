# 최소비용 구하기

from sys import stdin, setrecursionlimit
from collections import defaultdict

setrecursionlimit(1000000)

def calc_cost(cities):
  if not cities: return
  nxt_cities = set([])
  for city in cities:
    for city_d in ways[city].keys():
      if visited[city_d] > ways[city][city_d] + visited[city]:
        visited[city_d] = ways[city][city_d] + visited[city]
        nxt_cities.add(city_d)
  calc_cost(list(nxt_cities))

N = int(input())
M = int(input())

ways = defaultdict(dict)
visited = [100000**2 for _ in range(N+1)]

for _ in range(M):
  city_s, city_d, cost = map(int, stdin.readline().split())
  if city_d not in ways[city_s]: ways[city_s][city_d] = 100000**2
  ways[city_s][city_d] = min(ways[city_s][city_d], cost)

A, B = map(int, input().split())

visited[A] = 0

calc_cost([A])
print(visited[B])