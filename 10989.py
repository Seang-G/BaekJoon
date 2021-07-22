# 수 정렬하기3

import sys

count = [0] * (10000)

for _ in range(int(input())):
    count[int(sys.stdin.readline())-1] += 1

for i in range(10000):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i+1)