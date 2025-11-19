N = int(input())
nums = list(map(int,input().split()))

dp = [0] * N
dp[0] = 1

for i in range(1,N):
  temp = 0
  for j in range(i):
    if nums[j] < nums[i]:
      if dp[j] > temp:
        temp = dp[j]
  dp[i] = temp + 1

print(dp)
