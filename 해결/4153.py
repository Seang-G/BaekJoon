# 직각삼각형

T = sorted(list(map(int, input().split())))
while T != [0, 0, 0]:
    print('right' if T[0]**2 + T[1]**2 == T[2]**2 else 'wrong')
    T = sorted(list(map(int, input().split())))