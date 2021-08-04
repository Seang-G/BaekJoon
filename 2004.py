# 조합 0의 개수

n, m = map(int, input().split())

def f(n):
    s = 0
    for i in range(1, 100):
        if 0 == n//(5**i): break
        s += n//(5**i)
    return s

def t(n):
    s = 0
    for i in range(1, 1000):
        if 0 == n//(2**i): break
        s += n//(2**i)
    return s


print(max(0, min(f(n) - f(n-m) - f(m), t(n) - t(n-m) - t(m))))