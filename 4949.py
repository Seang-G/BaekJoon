# 균형잡힌 세상

from sys import stdin

S = stdin.readline().rstrip()
while S != '.':
    p = q = 0

    F = []
    for c in S:
        if c == '(':
            p += 1
            F.append(False)

        elif c == '[':
            q += 1
            F.append(True)

        elif c == ')':
            p -= 1
            if p < 0 or F.pop():
                print('no')
                break

        elif c == ']':
            q -= 1
            if q < 0 or not F.pop():
                print('no')
                break
    else:
        if p != 0 or q != 0: print('no')
        else: print('yes')

    S = stdin.readline().rstrip()