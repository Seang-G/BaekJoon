# 연산자 끼워넣기

N = int(input())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

Mx = -1000000001
Mn = 1000000001

def ysj(n, i, p, m, t, d):
    if i != N:
        a = A[i]
        if p: ysj(n+a, i+1, p-1, m, t, d)
        if m: ysj(n-a, i+1, p, m-1, t, d)
        if t: ysj(n*a, i+1, p, m, t-1, d)
        if d:
            if n < 0: ysj((abs(n)//a)*(-1), i+1, p, m, t, d-1)
            else: ysj(n//a, i+1, p, m, t, d-1)

    else:
        global Mx, Mn
        Mx = Mx if Mx > n else n
        Mn = Mn if Mn < n else n

ysj(A[0], 1, C[0], C[1], C[2], C[3])
print(Mx, Mn, sep='\n')