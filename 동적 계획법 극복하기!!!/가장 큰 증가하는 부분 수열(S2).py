N = int(input())
nums = list(map(int,input().split()))
dp = [nums[i] for i in range(N)]

for i in range(1,N):
  for j in range(i):
    print(dp)
    if nums[j] < nums[i]:
      dp[i] = max(dp[i], dp[j]+nums[i])

print(dp)
print(max(dp))