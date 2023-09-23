# 트리순회

def trav():
  pre_trav("A")
  in_trav("A")
  post_trav("A")

def pre_trav(node):
  if node == ".": return
  answers[0] += node
  pre_trav(tree[node][0])
  pre_trav(tree[node][1])

def in_trav(node):
  if node == ".": return
  in_trav(tree[node][0])
  answers[1] += node
  in_trav(tree[node][1])

def post_trav(node):
  if node == ".": return
  post_trav(tree[node][0])
  post_trav(tree[node][1])
  answers[2] += node

N = int(input())
tree = {}
answers = ["", "", ""]

for _ in range(N):
  parent, n1, n2 = input().split()
  tree[parent] = [n1, n2]

trav()
print(*answers, sep="\n")