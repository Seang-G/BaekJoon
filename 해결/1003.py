# 피보나치 함수

T = int(input())
f = [(1, 0), (0, 1)]
for i in range(2, 41):
    f.append((f[i-2][0] + f[i-1][0], f[i-2][1] + f[i-1][1]))

for _ in range(T):
    print(*f[int(input())])