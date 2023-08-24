# solved.ac

from sys import stdin

def round_f(val):
  return round(val+10**(-len(str(val))-1))

n = int(input())
cut = round_f(n*0.15)

opinions = []

for _ in range(n):
  opinions.append(int(stdin.readline().strip()))

opinions.sort()
if cut > 0: opinions = opinions[cut:-cut]
if n == 0: print(0)
else: print(round_f(sum(opinions)/len(opinions)))