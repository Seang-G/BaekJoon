# Hashing

r = 31
M = 1234567891
L = int(input())
chars = map(lambda x: ord(x)-ord("a")+1, list(input()))

answer = 0
for i, char in enumerate(chars):
  answer += char * r**i

print(answer%M)