# 덱

from collections import deque
from sys import stdin

N = int(input())

Q = deque([])
for _ in range(N):
    S = stdin.readline().split()

    if S[0] == 'push_front':
        Q.appendleft(S[1])

    elif S[0] == 'push_back':
        Q.append(S[1])

    elif S[0] == 'pop_front':
        if Q: print(Q.popleft())
        else: print(-1)

    elif S[0] == 'pop_back':
        if Q: print(Q.pop())
        else: print(-1)

    elif S[0] == 'size':
        print(len(Q))

    elif S[0] == 'empty':
        if Q: print(0)
        else: print(1)

    elif S[0] == 'front':
        if Q: print(Q[0])
        else: print(-1)

    elif S[0] == 'back':
        if Q: print(Q[-1])
        else: print(-1)