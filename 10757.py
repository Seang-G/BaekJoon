# 큰 수 A+B

A, B = input().split()
mx = max(len(A), len(B))
A = A.zfill(mx)
B = B.zfill(mx)
ans = ''
c = 0
for i in range(mx-1, -1, -1):
    c = int(A[i]) + int(B[i]) + c
    ans = str(c%10) + ans
    c //= 10
if c != 0: ans = '1' + ans
print(ans)