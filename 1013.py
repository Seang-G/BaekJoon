# Contact

def solve(wave):
  ptrn1 = False
  ptrn2 = False
  ptrn3 = False
  turning_point = False
  z_stack = 0
  o_stack = 0

  for i, bit in enumerate(wave):
    if ptrn1:
      if bit == "0": z_stack += 1
      elif z_stack < 2: return "NO"
      else: 
        ptrn1 = False
        ptrn3 = True
        o_stack = 1

    elif ptrn2:
      if bit == "0": return "NO"
      else: 
        ptrn2 = False

    elif ptrn3:
      if bit == "1": o_stack += 1
      if bit == "0":
        ptrn3 = False
        if o_stack >= 2: turning_point = True
        else: ptrn2 = True


    elif turning_point:
      if bit == "0":
        z_stack = 2
        ptrn1 = True
      turning_point = False

    elif bit == '1': 
      ptrn1 = True
      z_stack = 0

    elif bit == '0':
      ptrn2 = True

  if ptrn1 or ptrn2 or turning_point: return "NO"
  return "YES"

for _ in range(int(input())):
  wave = input()
  print(solve(wave))