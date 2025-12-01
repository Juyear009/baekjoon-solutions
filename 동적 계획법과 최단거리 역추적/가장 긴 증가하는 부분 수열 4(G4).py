N = int(input())
nums = list(map(int,input().split()))

dp = [1] * N

for i in range(1,N):
  for j in range(i):
    if nums[j] < nums[i]:
      dp[i] = max(dp[i], dp[j] + 1)

t = max(dp)
print(t)
idx = dp.index(t)
result = [nums[idx]]

for i in range(idx-1,-1,-1):
  if dp[i] == t - 1:
    t -= 1
    result.append(nums[i])

for i in range(len(result)-1,-1,-1):
  print(result[i], end=" ")