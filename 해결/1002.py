# 터렛

from math import sqrt

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    d = sqrt((x1-x2)**2 + (y1-y2)**2)
    r = r1 + r2
    
    if d > r: print(0)
    elif d == r: print(1)
    else:
        r = abs(r1-r2)
        if d == r: 
            if d == 0: print(-1)
            else: print(1)
        elif d < r: print(0)
        else: print(2)