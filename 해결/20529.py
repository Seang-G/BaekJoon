# 가장 가까운 세 사람의 심리적 거리

def calc_dist(mbti1, mbti2):
  return sum([1 for i in range(4) if mbti1[i]!=mbti2[i]])

T = int(input())

for _ in range(T):
  answer = 12
  N = int(input())
  if N >= 16*3:
    input()
    print(0)
    continue

  students = input().split()
  dists = [[calc_dist(mbti1, mbti2) for mbti2 in students] for mbti1 in students]
  
  for i in range(N): 
    for j, dist1 in enumerate(dists[i]):
      if i==j: continue
      for k, dist2 in enumerate(dists[i]):
        if i==k or j==k: continue
        answer = min(answer, dist1+dist2+dists[k][j])
  print(answer)
  
  