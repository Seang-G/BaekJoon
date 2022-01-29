# 저항

colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

dic = {}
for i in range(10):
    dic[colors[i]] = (i, 10**i)


print((dic[input()][0]*10 + dic[input()][0]) * dic[input()][1])