# 회전하는 큐

ln, M = map(int, input().split())
S = list(map(int, input().split()))

for i in range(M):
    for j in range(i+1, M):
        if S[i] < S[j]: S[j] -= 1

ans = 0
i = 1
for n in S:
    ans += min(abs(n-i), ln-abs(n-i))
    i = n
    ln -= 1

print(ans)