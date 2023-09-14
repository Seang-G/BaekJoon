# 오븐 시계

h, m = map(int, input().split())
c = int(input())

m += c
if m >= 60:
    h = (h+m//60)%24
    m %= 60
print(h, m)