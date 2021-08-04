# 오큰수

N = int(input())
A = list(map(int, input().split()))
O = [-1] * N
S = []

for i in range(N):
    while S:
        if A[S[-1]] < A[i]:
            O[S.pop()] = A[i]
        else: break
    S.append(i)

print(*O)