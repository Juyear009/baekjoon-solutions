N = int(input())
nums = list(map(int,input().split()))

dp = [[1,1] for _ in range(N)]

for i in range(1,N):
  if nums[i] >= nums[i-1]:
    dp[i][0] = dp[i-1][0] + 1
  if nums[i] <= nums[i-1]:
    dp[i][1] = dp[i-1][1] + 1

res = 0
for i in dp:
  res = max(i[0],i[1],res)

print(res)