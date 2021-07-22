# N과 M (4)

N, M = map(int, input().split())

def mk(st, lst, dep):
    if dep == M+1: 
        print(st[1:])
    else:
        for i, n in enumerate(lst):
            mk(st + ' ' + str(n), lst[i:], dep+1)

mk('', list(range(1, N+1)), 1)