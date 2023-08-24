# 게임

X, Y = map(int, input().split())

Z = Y*100//X

if X==Y or Z==99: print(-1)
else:
    low = 0
    high = 1000000000000

    while low < high:
      diff = (low+high)//2
      if Z == (Y+diff) * 100//(X+diff):
        low = diff+1
      else:
        high = diff
    print(high)