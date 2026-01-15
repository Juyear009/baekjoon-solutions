N = int(input())

dp = [100001 for _ in range(N+1)]

for i in range(1,N+1):
  if i in [1,2,5,7]:
    dp[i] = 1
  else:
    for c in [1,2,5,7]:
      if i >= c:
        dp[i] = min(dp[i],dp[i-c]+1)

if dp[N] == 100001:
  print(0)
else:
  print(dp[N])