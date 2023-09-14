# 화성 수학

from sys import stdin

T = int(input())

for _ in range(T):
    A = stdin.readline().split()
    A[0] = float(A[0])
    for c in A[1:]:
        if c == '@': A[0] *= 3
        elif c == '%': A[0] += 5
        else: A[0] -= 7
    
    print('{0:.2f}'.format(A[0]))