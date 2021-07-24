# 빠른 A+B

import sys
T = int(input())
for _ in range(T):
    n = sys.stdin.readline().rstrip().split()
    print(int(n[0])+int(n[1]))