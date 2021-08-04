# 괄호

from sys import stdin

T = int(input())

for _ in range(T):
    p = 0
    q = 0
    for v in stdin.readline().strip():
        if v == '(': p += 1
        else:
            q += 1
            if q > p: break
    else:
        if p == q:
            print('YES')
            continue
    print('NO')
    continue