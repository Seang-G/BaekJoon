# 이항 계수 1

from math import factorial as f

n, k = map(int, input().split())

print(f(n)//(f(k)*f(n-k)))