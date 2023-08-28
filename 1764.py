# 듣보잡

from sys import stdin
from collections import Counter

N, M = map(int, input().split())

sarams = [stdin.readline().strip() for _ in range(N+M)]
DBJs = [name for name, count in Counter(sarams).items() if count==2]

print(len(DBJs), *sorted(DBJs), sep="\n")