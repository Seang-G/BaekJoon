# 수 정렬하기

N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))

print(*sorted(lst), sep='\n')