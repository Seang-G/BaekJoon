# 경로찾기

from sys import stdin

N = int(input())

con_dic = {i:set([j for j, v in enumerate(stdin.readline().split()) if v=="1"]) for i in range(N)}

for _ in range(N):
  for i in range(N):
    for nv in list(con_dic[i]):
      con_dic[i].update(con_dic[nv])

answer = [["1" if j in con_dic[i] else "0" for j in range(N)] for i in range(N)]
print(*map(lambda x: " ".join(x), answer), sep="\n")