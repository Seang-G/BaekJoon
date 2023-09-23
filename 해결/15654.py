# N과 M (5)

from itertools import permutations as pm

N, M = map(int, input().split())

Ns = map(str, sorted(map(int, input().split())))
p = pm(Ns, M)
ans = map(lambda x: ' '.join(x), p)

print(*ans, sep='\n')