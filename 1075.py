# 나누기

N = int(input())
F = int(input())
for i in range(100):
    n = int(str(N)[:-2]+f'{i:0>2}')
    if int(n)%F == 0:
        print(f'{i:0>2}')
        break