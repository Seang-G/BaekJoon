# 01타일

a = 1
b = 2
N = int(input())
for i in range(3, N+1):
    temp = (a+b)%15746
    a = b
    b = temp
if N==1: print(1)
else: print(b)