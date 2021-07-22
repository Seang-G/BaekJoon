# N과 M (3)

N, M = map(int, input().split())
numbers = list(range(1, N+1))

def mk(st, dep):
    if dep == M+1: 
        print(st[1:])
    else:
        for n in numbers:
            mk(st + ' ' + str(n), dep+1)

mk('', 1)