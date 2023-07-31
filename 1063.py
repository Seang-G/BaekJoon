king_pos, dol_pos, N = input().split()

def check_is_out(col, row):
  if ord(col) < ord("A") or ord(col) > ord("H"):
    return True
  
  if row < 1 or row > 8:
    return True

  return False

def move(cur_pos, mov):
  col_pm = lambda col, pm: chr(ord(col)+pm)
  cur_col, cur_row = cur_pos[0], int(cur_pos[1])

  if "B" in mov:
    cur_row -= 1

  if "T" in mov:
    cur_row += 1
  
  if "L" in mov:
    cur_col = col_pm(cur_col, -1)
  
  if "R" in mov:
    cur_col = col_pm(cur_col, 1)
  
  return [check_is_out(cur_col, cur_row), cur_col+str(cur_row)]
  
for _ in range(int(N)):
  mov = input()
  
  is_out, next_king_pos = move(king_pos, mov)
  if is_out: continue

  if next_king_pos == dol_pos:
    is_out, next_dol_pos = move(dol_pos, mov)
    if is_out: continue
    dol_pos = next_dol_pos

  king_pos = next_king_pos
  

print(king_pos, dol_pos, sep="\n")