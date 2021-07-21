# 수 정렬하기2

import sys

N = int(input())
S = []
for _ in range(N):
    S.append(int(sys.stdin.readline()))

def partition(low, high):
    pivotitem = S[low]
    j = high
    i = low + 1
    while j >= i:
        if i < j: S[i], S[j] = S[j], S[i]
        i += 1
        j -= 1
    S[j], S[low] = S[low], S[j]
    return j

def quicksort(low, high):
    if high > low:
        pivotpoint = partition(low, high)
        quicksort(low, pivotpoint - 1)
        quicksort(pivotpoint + 1, high)

quicksort(0, len(S)-1)

print(S)