# 1, 2, 3 더하기

def dfs(lst):
  if sum(lst) <= 10:
    answers[sum(lst)] += 1
    for i in range(1, 4):
      dfs([*lst, i])

answers = [0 for _ in range(11)]
dfs([1])
dfs([2])
dfs([3])

for _ in range(int(input())):
  print(answers[int(input())])