# 전자레인지

T = int(input())
ABC = [5 * 60, 1 * 60, 10]

def DFS(t, n, lst):
    if t == 0:
        print(*lst)
        return True
        
    if n == 3: return False

    for i in range(t//ABC[n], -1, -1):
        lst[n] += i
        tf = DFS(t - ABC[n]*i, n+1, lst)
        lst[n] -= i
        if tf: exit(0)

    return False

if not DFS(T, 0, [0, 0, 0]): print(-1)