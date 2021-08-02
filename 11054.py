# 가장 긴 바이토닉 부분 수열

N = int(input())

A = list(map(int, input().split()))
inc = [1]*N
dec = [1]*N

for i in range(1, N):
    for j in range(i-1, -1, -1):
        if A[i] > A[j]:
            inc[i] = max(inc[j]+1, inc[i])
        if A[N-i-1] > A[N-j-1]:
            dec[N-i-1] = max(dec[N-j-1]+1, dec[N-i-1])

print(max(map(sum, zip(inc, dec)))-1)