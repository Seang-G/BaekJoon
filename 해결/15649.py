# N과 M (1)

from itertools import permutations as pm

N, M = map(int, input().split())

print(*map(lambda x: ' '.join(map(str, x)), pm(list(range(1, N+1)), M)), sep='\n')