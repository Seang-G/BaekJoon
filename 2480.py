# 주사위 세개

from collections import Counter as C

Dice = list(map(int, input().split()))

dic = C(Dice)

for die in Dice:
    if dic[die] == 3:
        print(10000+(die*1000))
        break
    elif dic[die] == 2:
        print(1000+(die*100))
        break
else: print(max(Dice)*100)