# 링

from math import gcd

N = int(input())
R = list(map(int, input().split()))

for n in R[1:]:
    g = gcd(R[0], n)
    print(f'{R[0]//g}/{n//g}')