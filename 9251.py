# LCS

S1 = 'x' + input()
S2 = 'x' + input()
ln1 = len(S1)
ln2 = len(S2)

if ln1 < ln2:
    S1, S2 = S2, S1
    ln1, ln2 = ln2, ln1

dp1 = [0] * ln2
dp2 = [0] * ln2

for i in range(1, ln1):
    for j in range(1, ln2):
        if S1[i] == S2[j]: dp1[j] = dp2[j-1] + 1
        else: dp1[j] = max(dp2[j], dp1[j-1])
    dp2 = dp1[:]

print(max(dp2))