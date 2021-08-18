# 숫자 카드 2

N = int(input())
NN = list(map(int, input().split()))

dic = {}
for n in NN:
    if n in dic: dic[n] += 1
    else: dic[n] = 1

M = int(input())
MM = list(map(int, input().split()))

for n in MM:
    try: print(dic[n], end=' ')
    except: print(0, end=' ')