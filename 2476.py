# 주사위 게임

from collections import Counter as C
from sys import stdin

N = int(input())
mx = 0
for _ in range(N):
    Dice = list(map(int, stdin.readline().split()))

    dic = C(Dice)

    for die in Dice:
        if dic[die] == 3:
            mx = max(mx, 10000+(die*1000))
            break
        elif dic[die] == 2:
            mx = max(mx, 1000+(die*100))
            break
    else: mx = max(mx, max(Dice)*100)

print(mx)