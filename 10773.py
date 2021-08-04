# 제로

from sys import stdin

K = int(input())

stack = []
for _ in range(K):
    n = int(stdin.readline())
    if n == 0: stack.pop()
    else: stack.append(n)

print(sum(stack))