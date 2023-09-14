# 파도반 수열

T = int(input())

P = [0, 1, 1, 1, 2] + [0]*96

for i in range(5, 101):
    P[i] = P[i-5] + P[i-1]

for _ in range(T): 
    print(P[int(input())])