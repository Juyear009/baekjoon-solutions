def dfs(x,y):
  global res
  visited[x][y] = True
  if graph[x][y] == "D":
    if not visited[x+1][y]:
      visited[x+1][y] = True
      dfs(x+1,y)
    elif visited[x+1][y] and not destiny[x+1][y]:
      res += 1
  elif graph[x][y] == "U":
    if not visited[x-1][y]:
      visited[x-1][y] = True
      dfs(x-1,y)
    elif visited[x-1][y] and not destiny[x-1][y]:
      res += 1
  elif graph[x][y] == "L":
    if not visited[x][y-1]:
      visited[x][y-1] = True
      dfs(x,y-1)
    elif visited[x][y-1] and not destiny[x][y-1]:
      res += 1
  elif graph[x][y] == "R":
    if not visited[x][y+1]:
      visited[x][y+1] = True
      dfs(x,y+1)
    elif visited[x][y+1] and not destiny[x][y+1]:
      res += 1
  destiny[x][y] = True

N,M = map(int,input().split())
graph = [list(input()) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
destiny = [[False] * M for _ in range(N)]
res = 0
for x in range(N):
  for y in range(M):
    if not visited[x][y]:
      dfs(x,y)
print(res)