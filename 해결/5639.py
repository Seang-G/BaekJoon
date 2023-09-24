# 이진 검색 트리

from sys import stdin, setrecursionlimit
from collections import defaultdict

setrecursionlimit(100000)

def grow(node, cur_node):
  if cur_node>node:
    if tree[cur_node][0] == 0: tree[cur_node][0] = node
    else: grow(node, tree[cur_node][0])
  else:
    if tree[cur_node][1] == 0: tree[cur_node][1] = node
    else: grow(node, tree[cur_node][1])

def post_trav(node):
  if not (tree[node][0] or tree[node][1]): 
    print(node)
    return
  if tree[node][0]: post_trav(tree[node][0])
  if tree[node][1]: post_trav(tree[node][1])
  print(node)

tree = {}

for i, node in enumerate(list(map(lambda x: int(x.strip()), stdin.readlines()))):
  tree[node] = [0, 0]
  if i: grow(node, root)
  else: root = node

post_trav(root)