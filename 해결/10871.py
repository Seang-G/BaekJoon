# X보다 작은 수

N, X = map(int, input().split())
lst = map(int, input().split())
for n in lst:
    if X > n: print(n, end=' ')