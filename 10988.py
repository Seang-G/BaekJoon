# 펠린드롬인지 확인하기

S = input()
SS = S[-1::-1]

if S==SS: print(1)
else: print(0)