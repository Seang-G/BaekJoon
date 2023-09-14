# 사분면 고르기

a = int(input())
b = int(input())
c = 1

if a*b > 0:
    if a < 0:c = 3
else:
    if a < 0:c = 2
    else: c = 4
print(c)