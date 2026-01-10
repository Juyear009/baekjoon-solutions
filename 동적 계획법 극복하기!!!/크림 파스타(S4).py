import sys

N = int(input())
nums = list(map(int,input().split()))
dp = [0 for _ in range(N)]
dp[0] = 0
minNum = nums[0]

for i in range(1,N):
  if minNum > nums[i]:
    minNum = nums[i]
  dp[i] = max(nums[i]-minNum,dp[i-1])

for i in dp:
  sys.stdout.write(str(i) + " ")