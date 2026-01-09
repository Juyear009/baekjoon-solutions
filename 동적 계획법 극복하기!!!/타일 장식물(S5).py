N = int(input())
dp = [0 for _ in range(N+1)]
dp[1] = 1
res = [0 for _ in range(N+1)]
res[1] = 4
for i in range(2,N+1):
  dp[i] = dp[i-1] + dp[i-2]
  res[i] = res[i-1] - dp[i] + dp[i] * 3

print(res[N])