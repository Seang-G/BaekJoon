# 피보나치 수 6

n = int(input())-1

def mul(A, B):
    lst = []
    for lstA in A:
        lst.append([])
        for lstB in B:
            S = 0
            for i in range(2):
                S += lstA[i] * lstB[i]
                S %= 1000000007
            lst[-1].append(S)
    return lst

def f(n):
    if n == -1: return [[0, 0]]
    if n == 0: return [[1, 0]]
    if n == 1: return [[1, 1], [1, 0]]
    else:
        lst = f(n//2)
        lst = mul(lst, list(zip(*lst)))
        if n%2 == 1: lst = mul(lst, [[1, 1], [1, 0]])
        return lst

print(mul(f(n), [[1, 0]])[0][0])