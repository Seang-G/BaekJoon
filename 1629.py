# 곱셈

A, B, C = map(int, input().split())

def f(n):
    if n == 1: return A%C
    return f(n//2)**2%C if n%2 == 0 else (f(n//2)**2 * A)%C

print(f(B))