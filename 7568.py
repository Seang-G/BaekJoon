# 덩치

n = int(input())
people = []
for i in range(n):
    people.append(list(map(int, input().split())))

for person in people:
    cnt = 0
    for i, other in enumerate(people):
        if other[0] > person[0] and other[1] > person[1]: cnt += 1
    print(cnt+1, end=' ')