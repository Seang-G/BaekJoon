# 명령 프롬프트

N = int(input())
ans = list(input())
for _ in range(N-1):
    st = list(input())
    for i in range(len(ans)):
        ans[i] = ans[i] if ans[i] == st[i] else '?'
print(''.join(ans))