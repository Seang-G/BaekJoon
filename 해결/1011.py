# Fly me to the Alpha Centauri
from bisect import bisect_left as bl

n = [0]
i = 0
while n[-1] <= 2147483648:
    n.append(n[-1]+i)
    i += 1
    n.append(n[-1]+i)
T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    print(bl(n, y-x) - 1)