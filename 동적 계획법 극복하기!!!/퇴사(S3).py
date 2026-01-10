N = int(input())
schedule = [list(map(int,input().split())) for _ in range(N)]

dp = [0 for _ in range(N+1)]

for i in range(N):
  dp[i+1] = max(dp[i+1],dp[i])
  if i + schedule[i][0] <= N:
    dp[i+schedule[i][0]] = max(dp[i+schedule[i][0]],dp[i]+schedule[i][1])


print(dp[N])