# 팰린드롬수

from sys import stdin

n = stdin.readline().strip()
while n != "0":
  if n==n[::-1]: print("yes")
  else: print("no")

  n = stdin.readline().strip()