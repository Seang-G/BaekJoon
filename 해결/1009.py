# 분산처리

from sys import stdin

dic = {0:[10]}
for i in range(1, 10):
    dic[i] = [i]
    n = (dic[i][-1]*i)%10
    while n != dic[i][0]:
        dic[i].append(n)
        n = (dic[i][-1]*i)%10

T = int(input())
for _ in range(T):
    a, b = map(int, stdin.readline().split())
    print(dic[a%10][b%len(dic[a%10])-1])