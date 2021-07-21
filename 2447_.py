# 별 찍기

from math import log

N = int(input())
k = int(log(N, 3))

st1 = '***'
st2 = '* *'
st2 = '   '

for i in range(N):
    for j in range(N//3):
        
    print()