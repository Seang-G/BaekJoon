# 수들의 합

S = int(input())

for i in range(10000000000):
    if S < i*(i+1)//2:
        print(i-1)
        break