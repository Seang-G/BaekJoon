# 터렛

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    ab = abs(x1-x2)**2 + abs(y1-y2)**2
    if ab == 0:
        
    c = (r1+r2)**2
    if ab>c: print(0)
    elif ab==c: print(1)
    else: print(2)