# 잃어버린 괄호

S = input()
N = ''
e = 0
for i in range(len(S)):
    if S[i] == '-':
        N += str(int(S[e:i])) + '-'
        e = i+1
    elif S[i] == '+':
        N += str(int(S[e:i])) + '+'
        e = i+1
N += str(int(S[e:]))

print(eval('-'.join(map(lambda x: str(eval(x)), N.split('-')))))