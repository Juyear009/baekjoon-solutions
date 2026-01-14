N,M = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(N)]

res = 0
for i in range(N):
  for j in range(M):
    if i <= N-4:
      res = max(res,g[i][j] + g[i+1][j] + g[i+2][j] + g[i+3][j])
    if j <= M-4:
      res = max(res,g[i][j] + g[i][j+1] + g[i][j+2] + g[i][j+3])
    if i <= N-2 and j <= M-2:
      res = max(res,g[i][j] + g[i+1][j] + g[i][j+1] + g[i+1][j+1])
    if  i <= N-3 and j <= M-2:
      res = max(res,g[i][j] + g[i+1][j] + g[i+2][j] + g[i+2][j+1])
      res = max(res,g[i][j+1] + g[i+1][j+1] + g[i+2][j+1] + g[i+2][j])
      res = max(res,g[i][j] + g[i+1][j] + g[i+2][j] + g[i][j+1])
      res = max(res,g[i][j+1] + g[i+1][j+1] + g[i+2][j+1] + g[i][j])

      res = max(res,g[i][j] + g[i+1][j] + g[i+1][j+1] + g[i+2][j+1])
      res = max(res,g[i][j+1] + g[i+1][j+1] + g[i+1][j] + g[i+2][j])

      res = max(res,g[i][j] + g[i+1][j] + g[i+2][j] + g[i+1][j+1])
      res = max(res,g[i][j+1] + g[i+1][j+1] + g[i+2][j+1] + g[i+1][j])
    if i <= N-2 and j <= M-3:
      res = max(res,g[i][j] + g[i][j+1] + g[i][j+2] + g[i+1][j+2])
      res = max(res,g[i][j] + g[i][j+1] + g[i][j+2] + g[i+1][j])
      res = max(res,g[i+1][j] + g[i+1][j+1] + g[i+1][j+2] + g[i][j])
      res = max(res,g[i+1][j] + g[i+1][j+1] + g[i+1][j+2] + g[i][j+2])

      res = max(res,g[i][j] + g[i][j+1] + g[i+1][j+1] + g[i+1][j+2])
      res = max(res,g[i+1][j] + g[i+1][j+1] + g[i][j+1] + g[i][j+2])

      res = max(res,g[i][j] + g[i][j+1] + g[i][j+2] + g[i+1][j+1])
      res = max(res,g[i+1][j] + g[i+1][j+1] + g[i+1][j+2] + g[i][j+1])

print(res)