N = int(input())
t = list(map(int,input().split()))

dp = [0] * N
dp[N-1] = 1

for i in range(N-2,-1,-1):
  if t[i] == 0:
    dp[i] = dp[i+1] + 1
  else:
    if i + t[i] + 1 >= N:
      dp[i] = 1
    else:
      dp[i] = dp[i+t[i]+1] + 1

for i in dp:
  print(i, end=" ")