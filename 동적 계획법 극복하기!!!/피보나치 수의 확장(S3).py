n = int(input())
dp = [0 for _ in range(abs(n)+1)]
dp[0] = 0
if abs(n) >= 1:
  dp[1] = 1

if n < 0:
  for i in range(-2,n-1,-1):
    t = (dp[abs(i)-2] - dp[abs(i)-1])
    if t >= 0:
      dp[abs(i)] = t % 1000000000
    else:
      dp[abs(i)] = -(abs(t) % 1000000000)
elif n > 0:
  for i in range(2,n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000000

if dp[-1] > 0:
  print(1)
elif dp[-1] == 0:
  print(0)
elif dp[-1] < 0:
  print(-1)

print(abs(dp[-1]))