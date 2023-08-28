# 바이러스

def dfs(connected_coms):
  for com in connected_coms:
    if visited[com]: continue
    visited[com] = True
    dfs(dic[com])

dic = {i:set([]) for i in range(1, int(input())+1)}

for _ in range(int(input())):
  com1, com2 = map(int, input().split())
  dic[com1].add(com2)
  dic[com2].add(com1)

visited = [False for _ in range(len(dic)+1)]
visited[1] = True

dfs(dic[1])
print(visited.count(True)-1)