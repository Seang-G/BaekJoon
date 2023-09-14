# ATM

import heapq

N = int(input())

q = []
for n in list(map(int, input().split())):
    heapq.heappush(q, n)

ans = 0
for i in range(N, 0, -1):
    ans += heapq.heappop(q)*i

print(ans)

# N = int(input())
# P = list(map(int, input().split()))
# P.sort()

# ans = 0
# for i in range(N):
#     ans += P[i]*(N-i)

# print(ans)