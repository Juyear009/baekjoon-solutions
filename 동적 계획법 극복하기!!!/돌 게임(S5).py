N = int(input())

dp = [0] * N

dp[0] = 1

for i in range(1,N):
  dp[i] = dp[i-1] + 1

if N % 2 == 0:
  print("CY")
else:
  print("SK")
