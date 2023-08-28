# 숨바꼭질

N, K = map(int, input().split())

def odd(k, depth=1, visited=[]):
  return min(even(k-1, depth+1, visited.copy()), even(k+1, depth+1, visited.copy()))

def even(k, depth=1, visited=[]):
  if k<0 or k in visited: return 100000000
  visited.append(k)
  if k%2 == 0:
    if k//2 <= N: return min(k-N+depth-1, N-k//2+depth)
    else: 
      return even(k//2, depth+1, visited.copy())
  else: return odd(k, depth, visited.copy())

if N >= K: print(N-K)
elif K%2 == 0: print(even(K))
else: print(odd(K))