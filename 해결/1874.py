# 스택 수열

from sys import stdin

n = int(input())

q = []
for _ in range(n):
    q.append(int(stdin.readline()))

q = q[-1::-1]
stack = []
ans = []

for i in range(1, n+1):
    stack.append(i)
    ans.append('+')
    while True:
        if stack and stack[-1] == q[-1]:
            ans.append('-')
            stack.pop()
            q.pop()
        elif stack and stack[-1] > q[-1]:
            ans = ['NO']
            break
        else: break
    if ans[0] == 'NO': break

print(*ans, sep='\n')