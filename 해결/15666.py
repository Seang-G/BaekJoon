# N과 M (12)

def lee(ans, i, depth):
  if depth == M:
    print(ans)
    return

  for j, n in enumerate(Ns[i:]):
    lee(f"{ans} {n}", i+j, depth+1)


N, M = map(int, input().split())
Ns = sorted(map(int, list(set(input().split()))))

for i, n in enumerate(Ns):
  lee(f"{n}", i, 1)