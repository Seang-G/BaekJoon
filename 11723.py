# 집합

from sys import stdin

S = set([])
for _ in range(int(input())):
  oper = stdin.readline().strip().split()

  if oper[0] == "add": S.add(int(oper[1]))
  elif oper[0] == "remove": S.difference_update({int(oper[1])})
  elif oper[0] == "check": print(1 if int(oper[1]) in S else 0)
  elif oper[0] == "toggle": S.symmetric_difference_update({int(oper[1])})
  elif oper[0] == "all": S = set(range(1, 21))
  elif oper[0] == "empty": S = set([])