# 스택

import sys

N = int(input())

stack = []
for _ in range(N):
    S = sys.stdin.readline().split()

    if S[0] == 'push':
        stack.append(S[1])

    elif S[0] == 'pop':
        if stack: print(stack.pop())
        else: print(-1)

    elif S[0] == 'size':
        print(len(stack))

    elif S[0] == 'empty':
        if stack: print(0)
        else: print(1)

    else:
        if stack: print(stack[-1])
        else: print(-1)