N = int(input())

dp = [float('inf')] * (N + 1)
dp[N] = 0
if N % 3 == 0:
  dp[N//3] = 1
if N % 2 == 0:
  dp[N//2] = 1

for i in range(N-1,1,-1):
  if dp[i+1] != float('inf'):
    dp[i] = min(dp[i], dp[i+1] + 1)
    if i % 3 == 0:
      dp[i//3] = min(dp[i//3], dp[i] + 1)
    if i % 2 == 0:
      dp[i//2] = min(dp[i//2], dp[i] + 1)

t = dp[1]
result = [1]
for i in range(2,N+1):
  if dp[i] == t-1:
    if result[-1] * 3 == i or result[-1] * 2 == i or result[-1] + 1 == i:
      t -= 1
      result.append(i)

print(dp[1])

for i in range(len(result)-1,-1,-1):
  print(result[i], end=" ")
