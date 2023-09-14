# 하노이 탑 이동 순서

csq = []

def mv(n, st, el, dn):
    if n == 1:
        csq.append((st, dn))
        return
    mv(n-1, st, dn, el)
    csq.append((st, dn))
    mv(n-1, el, st, dn)

mv(int(input()), 1, 2, 3)

print(len(csq))
for c in csq:
    print(c[0], c[1])