# 배수와 약수

n, m = map(int, input().split())
while n != 0 or m != 0:
    if n%m == 0: print('multiple')
    elif m%n == 0: print('factor')
    else: print('neither')
    n, m = map(int, input().split())