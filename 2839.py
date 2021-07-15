# 설탕 배달

lst = [-999, -999, -999, 1, -999, 1, 2, -999, 2, 3, 2, 3, 4, 3, 4]
N = int(input())
for i in range(15, N+1):lst.append(lst[i-5]+1)
print(lst[N] if lst[N]>0 else -1)