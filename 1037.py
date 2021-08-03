# 약수

N = int(input())
S = list(map(int, input().split()))
S.sort()

print(S[0]*S[-1])