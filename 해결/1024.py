# 수열의 합

N, L = map(int, input().split())

for i in range(L, 101):
    if i%2 == 0 and (N/i - N//i) == 0.5 and N//i-i//2+1 >= 0:
        print(*list(range(N//i-i//2+1, N//i+i//2+1)))
        break

    elif i%2 == 1 and float(N//i) == N/i and N//i-i//2 >= 0:
        print(*list(range(N//i-i//2, N//i+i//2+1)))
        break

else: print(-1)