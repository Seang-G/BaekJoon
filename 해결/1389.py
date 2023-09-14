# 케빈 베이컨의 6단계 법칙

def bfs(me, candidates, depth):
  if -1 in kbs[me]: 
    next_candidates = set([])

    for candidate in list(candidates):
      if kbs[me][candidate] == -1:
        kbs[me][candidate] = depth
      next_candidates.update(dic[candidate])

    bfs(me, next_candidates, depth+1)

N, M = map(int, input().split())

kbs = [[-1 if i!=j else 0 for i in range(N)] for j in range(N)]
dic = {i:[] for i in range(N)}
kbns = {i+1:0 for i in range(N)}

for _ in range(M):
  per1, per2 = map(lambda x: int(x)-1, input().split())
  dic[per1].append(per2)
  dic[per2].append(per1)

for me in range(N):
  bfs(me, set(dic[me]), 1)
  kbns[me+1] = sum(kbs[me])

answer = sorted(kbns.items(), key=lambda x: x[1])[0][0]

print(answer)