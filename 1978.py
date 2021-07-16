# 소수 찾기

che = list(range(2, 1001))
for n in che:
    for x in range(n*2, 1001, n):
        try: che.remove(x)
        except: continue
input()
print(len(set(map(int, input().split())) & set(che)))