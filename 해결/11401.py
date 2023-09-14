# 이항 계수 3

N, K = map(int, input().split())
p = 1000000007
A = max(N-K, K)
B = N-A

S = 1
SS = 1
for i in range(2, N+1):
    S *= i
    S %= p
    if i == N-K: SS *= S
    if i == K: SS *= S

SS = SS % p

def f(SS, k):
    if k == 1: return SS 
    return f(SS, k//2)**2%p if k%2 == 0 else (f(SS, k//2)**2*SS)%p

print(f(SS, p-2)*S%p)