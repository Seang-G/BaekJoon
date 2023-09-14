# 가장 긴 증가하는 부분 수열

N = int(input())

A = list(map(int, input().split()))
S = [1]*N

for i in range(1, N):
    for j in range(i-1, -1, -1):
        if A[i] > A[j]:
            S[i] = max(S[j]+1, S[i])
            
print(max(S))