#부녀회장이 될테야

T = int(input())
apart = [list(range(1, 15))]+[[1] for _ in range(14)]

for i in range(1, 15):
    for j in range(1, 14):
        apart[i].append(apart[i][j-1]+apart[i-1][j])

for _ in range(T):
    print(apart[int(input())][int(input())-1])