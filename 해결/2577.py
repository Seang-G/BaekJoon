# 숫자의 개수

A = [0]*10

N = int(input())
N *= int(input())
N *= int(input())

for v in str(N): A[int(v)] += 1
print(*A, sep='\n')