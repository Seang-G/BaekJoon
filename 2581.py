# 소수

from bisect import bisect_right as br, bisect_left as bl 

che = list(range(2, 10001))
for n in che:
    for x in range(n*2, 10001, n):
        try: che.remove(x)
        except: continue

lst = che[bl(che, int(input())):br(che, int(input()))]
try: print(sum(lst), lst[0], sep='\n')
except: print(-1)