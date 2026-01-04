import sys
from collections import deque

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(x,y):
  a = find(x)
  b = find(y)
  if a != b:
    parent[b] = a
    return True
  return False

def bfs(i,j,n):
  queue = deque([(i,j)])
  while queue:
    x,y = queue.popleft()
    for dx,dy in dist:
      newx = x + dx
      newy = y + dy
      if 0 <= newx < N and 0 <= newy < M:
        if (newx,newy) not in visited and graph[newx][newy] == 1:
          queue.append((newx,newy))
          graph[newx][newy] = n
          visited.add((newx,newy))

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
islandCnt = 0
dist = [(0,1),(0,-1),(1,0),(-1,0)]
visited = set()
for i in range(N):
  for j in range(M):
    if graph[i][j] == 1 and (i,j) not in visited:
      islandCnt += 1
      graph[i][j] = islandCnt
      visited.add((i,j))
      bfs(i,j,islandCnt)

edges = []
parent = [i for i in range(islandCnt+1)]
for x in range(N):
  for y in range(M):
    if graph[x][y] != 0:
      for dx, dy in dist:
        newx = x
        newy = y
        cnt = 0
        while True:
          newx += dx
          newy += dy
          if 0 <= newx < N and 0 <= newy < M:
            if graph[newx][newy] == 0:
              cnt += 1
              continue
            elif graph[newx][newy] != graph[x][y] and cnt > 1:
                edges.append((cnt,graph[x][y],graph[newx][newy]))
            break
          else:
            break

edges.sort()
mst = 0
cnt = 0
for c,x,y in edges:
  if union(x,y):
    mst += c
    cnt += 1
    if cnt == islandCnt-1:
      break

if cnt != islandCnt-1 or mst == 0:
  print(-1)
else:
  print(mst)
