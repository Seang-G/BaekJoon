# 사분면

from sys import stdin

n = int(input())
Q = [0]*5

for _ in range(n):
    x, y = map(int, stdin.readline().split())
    if x > 0:
        if y > 0: Q[1] += 1
        elif y < 0: Q[4] += 1
        else: Q[0] += 1
    elif x < 0:
        if y > 0: Q[2] += 1
        elif y < 0: Q[3] += 1
        else: Q[0] += 1
    else: Q[0] += 1

for i in range(1, 5):
    print(f'Q{i}: {Q[i]}')

print(f'AXIS: {Q[0]}')