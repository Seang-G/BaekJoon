# 수 정렬하기2

import sys

N = int(input())
S = []
S.append(int(sys.stdin.readline()))

S.sort()

print(*S, sep='\n')