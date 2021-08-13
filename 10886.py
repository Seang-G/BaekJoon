# 0 = not cute / 1 = cute

from sys import stdin

N = int(input())
dic = {'0':0, '1':0}

for _ in range(N):
    dic[stdin.readline().strip()] += 1

if dic['0'] > dic['1']: print('Junhee is not cute!')
else: print('Junhee is cute!')