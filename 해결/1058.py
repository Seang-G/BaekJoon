# 친구

from collections import Counter

N = int(input())

people = []
people_tf = []
for _ in range(N):
  people.append(input())
  people_tf.append([0 for _ in range(N)])

for i, human in enumerate(people):
  for j, friend in enumerate(human):
    if friend == "Y":
      people_tf[i][j] = 1
      for k, ffriend in enumerate(people[j]):
        if ffriend == "Y":
          people_tf[i][k] = 1

for i in range(N):
  people_tf[i][i] = 0

print(max(list(map(lambda x: Counter(x)[1], people_tf))))