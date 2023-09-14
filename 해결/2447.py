# 별 찍기

from math import log

N = int(input())
k = round(log(N, 3))
stars = [['***', '* *', '***']] + [['' for _ in range(3**(i+1))] for i in range(1, k)]

for i in range(1, k):
    for j in range(3**(i+1)):
        if (j//(3**i)) == 1: stars[i][j] += stars[i-1][j%len(stars[i-1])]+' '*len(stars[i-1][j%len(stars[i-1])])+stars[i-1][j%len(stars[i-1])]
        else: stars[i][j] += stars[i-1][j%len(stars[i-1])]*3

for star in stars[-1]:
    print(star)