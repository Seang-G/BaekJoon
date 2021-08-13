# 학점계산

dic_A = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.0}
dic_O = {'+':0.3, '0':0.0, '-':-0.3}

C = input()
if C == 'F': print(dic_A[C])
else: print(dic_A[C[0]]+dic_O[C[1]])