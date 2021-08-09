# AC

from sys import stdin
from collections import deque

T = int(input())

for _ in range(T):
    Ord = stdin.readline().strip().replace('RR', '')
    n = int(stdin.readline())
    A = stdin.readline().strip()[1:-1]
    if A: A = A.split(',')
    A = deque(A)

    R = False
    for o in Ord:
        if o == 'R':
            R = not(R)
        else:
            try:
                if R: A.pop()
                else: A.popleft()
            except:
                print('error')
                break
    else:
        if R: print('[' + ','.join(list(A)[-1::-1]) + ']')
        else: print('[' + ','.join(list(A)) + ']')