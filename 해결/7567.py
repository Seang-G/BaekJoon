# 그릇

A = input()
gr = A[0]
S = 10
for g in A[1:]:
    if gr == g: S += 5
    else:
        S += 10
        gr = g
print(S)