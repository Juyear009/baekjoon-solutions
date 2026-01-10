n = int(input())

dp = [0 for _ in range(n+1)]
dp[0] = 1

for i in range(1,n+1):
  t = 0
  for j in range(i):
    t += dp[j] * dp[i-j-1]
  dp[i] = t

print(dp[-1])