# Quadrant => qdr (사분면)
def calc_qdr(n, row, col):
  qdr_table = {
    "LU": 1,
    "RU": 2,
    "LD": 3,
    "RD": 4
  }
  cr_n = (2**n)//2
  rlud = ("L" if col<cr_n else "R") + ("U" if row<cr_n else "D")

  if "R" in rlud: col -= cr_n
  if "D" in rlud: row -= cr_n

  if n==1: return [qdr_table[rlud]]
  return [qdr_table[rlud], *calc_qdr(n-1, row, col)]

N, r, c =  map(int, input().split())
qdr_lst = calc_qdr(N, r, c)

sm = 0
for i, qdr in enumerate(qdr_lst):
  inc = 4**(N-i-1)
  sm += inc*(qdr-1)

print(sm)