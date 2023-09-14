# 비밀번호 찾기

from sys import stdin

N, M = map(int, input().split())

password_manager = {}
for _ in range(N):
  url, password = stdin.readline().strip().split()
  password_manager[url] = password
  
for _ in range(M):
  url = stdin.readline().strip()
  password = password_manager[url]
  print(password)