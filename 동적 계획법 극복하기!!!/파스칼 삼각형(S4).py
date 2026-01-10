R,C,W = map(int,input().split())

dp = [[1 for _ in range(R+W)] for _ in range(R+W)]

for i in range(3,R+W):
  for j in range(2,i):
    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

res = 0
for i in range(R,R+W):
  for j in range(C,i-R+C+1):
    res += dp[i][j]

print(res)