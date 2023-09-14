# 좌표 압축

N = int(input())
S = list(map(int, input().split()))

dic_idx = {}
SS = sorted(list(set(S)))

for i, n in enumerate(SS): dic_idx[n] = i

for n in S: print(dic_idx[n], end=' ')