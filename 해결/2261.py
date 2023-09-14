# 가장 가까운 두 점

import time
from sys import stdin
import bisect
from math import sqrt

dup = False
dic = {}

f = open("C:\\Users\\mgw77\\OneDrive\\바탕 화면\\Algo\Temp\\1.in.txt", 'r')
n = int(f.readline())
# n = int(input())

for _ in range(n):
    # a, b = map(int, stdin.readline().split())
    a, b = map(int, f.readline().split())
    if a in dic:
        if b in dic[a]: dup = True
        dic[a].append(b)
    else: dic[a] = [b]

start = time.time()

if dup: print(0)
else:
    keys = sorted(dic.keys())
    for key in keys: dic[key].sort()

    mn = 20000**2 + 20000**2

    for x in keys:
        ys = dic[x]
        for j in range(len(ys)-1):
            mn = min(mn, (ys[j+1] - ys[j])**2)

    for i, x in enumerate(keys[1:], start=1):
        for y in dic[x]:
            ii = i-1
            xx = keys[ii]
            lx = x-sqrt(mn)
            while xx > lx and ii >= 0:
                r = bisect.bisect_left(dic[xx], y)
                d = sqrt(mn-(x-xx)**2)
                if r < len(dic[xx]) and y-d < dic[xx][r] < y+d:
                    yy = dic[xx][r]
                    xy = (x-xx)**2 + (y-yy)**2
                    if mn > xy:
                        mn = xy
                        lx = x-sqrt(mn)

                if 0 <= r-1 and y-d < dic[xx][r-1] < y+d:
                    yy = dic[xx][r-1]
                    xy = (x-xx)**2 + (y-yy)**2
                    if mn > xy:
                        mn = xy
                        lx = x-sqrt(mn)
                
                ii -= 1
                xx = keys[ii]
    print(mn)

print(time.time() - start)