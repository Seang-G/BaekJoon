# 신나는 함수 실행

f = {}
for a in range(-1, 21):
    for b in range(-1, 21):
        for c in range(-1, 21):
            if a <= 0 or b <= 0 or c <= 0: f[(a, b, c)] = 1
            elif a < b and b < c: f[(a, b, c)] = f[(a, b, c-1)] + f[(a, b-1, c-1)] - f[(a, b-1, c)]
            else: f[(a, b, c)] = f[(a-1, b, c)] + f[(a-1, b-1, c)] + f[(a-1, b, c-1)] - f[(a-1, b-1, c-1)]

a, b, c = map(int, input().split())
while a != -1 or b != -1 or c != -1:
    if a <= 0 or b <= 0 or c <= 0: f[(a, b, c)] = 1
    elif a > 20 or b > 20 or c > 20: f[(a, b, c)] = f[(20, 20, 20)]
    print(f'w({a}, {b}, {c}) = {f[(a, b, c)]}')
    a, b, c = map(int, input().split())