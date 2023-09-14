# 주사위 게임

n = int(input())

c = 100
s = 100

for _ in range(n):
    a, b = map(int, input().split())
    
    if a > b: s -= a
    elif a < b: c -= b

print(c, s, sep = '\n')