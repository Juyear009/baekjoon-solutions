N = int(input())
dp = [False] * N

for i in range(1,N):
  if dp[i-1] == False or (i >= 3 and dp[i-3] == False):
    dp[i] = True

if dp[-1]:
  print("SK")
else:
  print("CY")