N = int(input())
schedule = [list(map(int,input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
  for j in range(i,schedule[i][0]+i):
    if schedule[i][0] + i > N:
      continue
    dp[i][j] = schedule[i][1]

for i in range(1,N):
  for j in range(i):
    if dp[j][i] == 0:
      for k in range(i,schedule[i][0]+i):
        if schedule[i][0] + i > N:
          continue
        dp[i][k] = max(dp[i][k],max(dp[j])+schedule[i][1])


res = 0
for i in dp:
  for j in i:
    res = max(res,j)

print(res)