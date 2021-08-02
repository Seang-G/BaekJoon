# 1로 만들기

from collections import deque 

N = int(input())
mx = N+1
S = [mx] * (mx)
S[N] = 0

q = deque([N])
while q:
    n = q.popleft()

    if n//3 != 0:
        S[n//3] = min(S[n] + n%3 + 1, S[n//3])
        q.append(n//3)

    if n//2 != 0:
        S[n//2] = min(S[n] + n%2 + 1, S[n//2])
        q.append(n//2)

print(S[1])