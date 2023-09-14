# 기타줄

N, M = map(int, input().split())

pp = 1000
ss = 1000
for _ in range(M):
    p, s = map(int, input().split())
    pp = min(pp, p)
    ss = min(ss, s)

if N%6 > 0:
    print(min([pp*(N//6) + ss*(N%6), ss*N, pp*(N//6+1)]))
else:
    print(min([pp*(N//6) + ss*(N%6), ss*N]))