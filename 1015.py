# 수열 정렬

N = int(input())
A = list(map(int, input().split()))
AA = sorted(A)
B = []
for i in range(N):
    ii = AA.index(A[i])
    B.append(ii)
    AA[ii] = -1

print(*B)