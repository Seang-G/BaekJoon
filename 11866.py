# 요세푸스 문제 0

N, K = map(int, input().split())
q = list(range(1, N+1))
s = []
ln = N

i = K-1
while q:
    s.append(str(q.pop(i)))
    ln = max(ln-1, 1)
    i = (i+K-1)%ln

print('<' + ', '.join(s) + '>')