# 카드2

from collections import deque

N = int(input())
q = deque(list(range(N, 0, -1)))

i = N
while i > 1:
    q.pop()
    q.appendleft(q.pop())
    i -= 1

print(*q)