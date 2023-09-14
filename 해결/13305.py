# 주유소

N = int(input())

dr = list(map(int, input().split()))
ds = list(map(int, input().split()))

ans = dr[0] * ds[0]
for i in range(1, N-1):
    ds[i] = min(ds[i], ds[i-1])
    ans += dr[i] * ds[i]

print(ans)