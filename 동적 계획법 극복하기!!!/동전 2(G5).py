n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]

dp = [10001 for _ in range(k+1)]

for c in coins:
  if c <= k:
    dp[c] = 1

for i in range(1,k+1):
  for c in coins:
    if i >= c:
      dp[i] = min(dp[i],dp[i-c]+1)

if dp[-1] == 10001:
  print(-1)
else:
  print(dp[-1])