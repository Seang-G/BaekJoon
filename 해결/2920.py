# 음계

playing = list(map(int, input().split()))

if playing == [i for i in range(1, 9)]: print("ascending")
elif playing == [i for i in range(8, 0, -1)]: print("descending")
else: print("mixed")