# Four Squares

n = int(input())

def solve(n):
  for i in range(int(50000**0.5)+1):
    for j in range(i, int(50000**0.5)+1):
      if i**2 + j**2 > 50000: break
      for k in range(j, int(50000**0.5)+1):
        if i**2 + j**2 + k**2 > 50000: break
        if n == i**2 + j**2 + k**2: 
          if i == 0 and j == 0: return 1
          elif i == 0 or j == 0: return 2
          else: return 3
  return 4

print(solve(n))