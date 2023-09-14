# N-Queen

N = int(input())
cnt = 0

lst = [0] * N

def ck(i):
    for j in range(i):
        if lst[i] == lst[j] or abs(lst[i] - lst[j]) == i-j: return False
    return True

def NQ(i):
    global cnt
    if i == N: cnt += 1
    else:
        for j in range(N):
            lst[i] = j
            if ck(i): NQ(i+1)

NQ(0)
print(cnt)