# 큐

from sys import stdin

queue = []

for _ in range(int(input())):
  order = stdin.readline().strip().split()
  
  if order[0] == "push":
    queue.append(int(order[1]))
  
  elif order[0] == "pop":
    if len(queue) == 0: print(-1)
    else: print(queue.pop(0))

  elif order[0] == "size":
    print(len(queue))

  elif order[0] == "empty":
    if queue: print(0)
    else: print(1)

  elif order[0] == "front":
    if len(queue) == 0: print(-1)
    else: print(queue[0])

  elif order[0] == "back":
    if len(queue) == 0: print(-1)
    else: print(queue[-1])