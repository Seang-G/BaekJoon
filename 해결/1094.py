# 막대기

X = float(input())
sticks = [64]

while X != sum(sticks):
  mn = sticks.pop()
  sticks.append(mn/2)
  if X > sum(sticks): sticks.append(mn/2)

print(len(sticks))