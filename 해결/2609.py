# 최대공약수와 최소공배수

import math

n, m = map(int, input().split())
g = math.gcd(n, m)
print(g, n*m//g, sep='\n')