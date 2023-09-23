# DSLR

from sys import setrecursionlimit, stdin

# 깊이 제한을 너무 크게 잡으면 메모리 초과남.
# 100,000정도가 적당한 듯?
setrecursionlimit(100000)

def case(lst):
  nxt = []
  for v, dslr in lst:
    for i in range(4):
      if memo[dic[v][i]]: continue
      if dic[v][i] == goal: return dslr+dslr_lst[i]
      nxt.append((dic[v][i], dslr+dslr_lst[i]))
      memo[dic[v][i]] = True
  return case(nxt.copy())

dslr_lst = ["D", "S", "L", "R"]

dic = {i:[i*2%10000, (i+9999)%10000, int(str(i).zfill(4)[1:]+str(i).zfill(4)[0]), int(str(i).zfill(4)[-1]+str(i).zfill(4)[:-1])] for i in range(10000)}

T = int(input())
for _ in range(T):
  memo = [False for __ in range(10000)]
  start, goal = map(int, stdin.readline().strip().split())
  print(case([(start, "")]))