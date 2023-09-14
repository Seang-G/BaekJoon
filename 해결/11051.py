# 이항 계수 2

n, k = map(int, input().split())

f = [1]*n
for i in range(1, n):
    f[i] = f[i-1] * (i+1)
    
print(f[n-1]//(f[k-1]*f[n-k-1])%10007)