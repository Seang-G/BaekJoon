# N과 M (9)

from itertools import permutations as pm

N, M = map(int, input().split())

Ns = map(str, sorted(map(int, input().split())))

print(*map(lambda x: ' '.join(x), list(dict.fromkeys(pm(Ns, M)))), sep='\n')