# A+B - 3

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
for ns in lst:
    print(ns[0]+ns[1])