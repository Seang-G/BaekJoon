# 개표

from collections import Counter as C

V = int(input())
dic = C(input())
if dic['A'] > dic['B']: print('A')
elif dic['A'] < dic['B']: print('B')
else: print('Tie')