# 최소공배수

import math

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(n*m//math.gcd(n, m))