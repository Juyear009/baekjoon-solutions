N = int(input())
dp1 = [0,0,0]
dp2 = [0,0,0]
scores = list(map(int,input().split()))

for i in range(3):
  dp1[i] = scores[i]
  dp2[i] = scores[i]

for i in range(1,N):
  scores = list(map(int,input().split()))
  t1 = [0,0,0]
  t1[0] = max(dp1[:2]) + scores[0]
  t1[1] = max(dp1) + scores[1]
  t1[2] = max(dp1[1:]) + scores[2]
  dp1 = t1

  t2 = [0,0,0]
  t2[0] = min(dp2[:2]) + scores[0]
  t2[1] = min(dp2) + scores[1]
  t2[2] = min(dp2[1:]) + scores[2]
  dp2 = t2

print(max(dp1), min(dp2))

