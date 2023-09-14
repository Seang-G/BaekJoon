# 폐션왕 신해빈

T = int(input())

for _ in range(T):
    N = int(input())
    dic = {}

    for _ in range(N):
        c = input().split()
        if c[1] not in dic: dic[c[1]] = []
        dic[c[1]].append(c[0])
    lst = list(map(len, list(dic.values())))

    S = 0
    for n in lst:
        S += (n*S) + n
        
    print(S)