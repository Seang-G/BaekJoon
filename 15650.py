# N과 M (2)

from itertools import combinations as cb

N, M = map(int, input().split())

print(*map(lambda x: ' '.join(map(str, x)), cb(list(range(1, N+1)), M)), sep='\n')