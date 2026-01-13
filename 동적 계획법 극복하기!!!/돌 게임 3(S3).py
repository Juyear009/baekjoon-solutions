N = int(input())
dp = [False] * (N+1)
dp[1] = True
if N >= 3:
  dp[3] = True
if N >= 4:
  dp[4] = True

for i in range(5,N+1): 
  if dp[i-1] == False or dp[i-3] == False or dp[i-4] == False:
    dp[i] = True
  
if dp[-1]:
  print("SK")
else:
  print("CY")