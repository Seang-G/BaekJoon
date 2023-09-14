# Yangjojang of The Year

from sys import stdin

T = int(input())
for _ in range(T):
    dic = {}
    N = int(stdin.readline())
    for i in range(N):
        k, v = stdin.readline().split()
        dic[k] = int(v)
    print(sorted(dic.items(), key=lambda x: x[1], reverse=True)[0][0])