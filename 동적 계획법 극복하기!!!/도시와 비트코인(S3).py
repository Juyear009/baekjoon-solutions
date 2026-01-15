N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(M)]

dp = [[False] * N for _ in range(M)]
dp[0][0] = True

for i in range(M):
  for j in range(N):
    if graph[i][j] != 0:
      if j > 0 and dp[i][j-1]:
        dp[i][j] = True
      elif i > 0 and dp[i-1][j]:
        dp[i][j] = True

if dp[M-1][N-1]:
  print("Yes")
else:
  print("No")