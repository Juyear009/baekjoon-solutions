import sys
from collections import deque
import heapq

def bfs():
  global shark
  queue = deque([(0,shark[0],shark[1])])
  visited = set()
  visited.add((shark[0],shark[1]))
  d = [(-1,0),(0,-1),(1,0),(0,1)]
  fishes = []
  min_level = None
  while queue:
    l,x,y = queue.popleft()
    if min_level != None and l > min_level:
      break
    if 0 < graph[x][y] < shark[2]:
      heapq.heappush(fishes,(l,x,y))
      min_level = l
      continue

    for i in range(4):
      newX = x + d[i][0]
      newY = y + d[i][1]
      if 0 <= newX < N and 0 <= newY < N:
        if (newX,newY) not in visited and graph[newX][newY] <= shark[2]:
          queue.append((l+1,newX,newY))
          visited.add((newX,newY))

  if len(fishes) == 0:
    return False
  l,x,y = heapq.heappop(fishes)
  if (shark[3]+1)%shark[2] == 0:
    shark = (x,y,shark[2]+1,0)
  else:
    shark = (x,y,shark[2],shark[3]+1)
  graph[x][y] = 0
  return l


input = sys.stdin.readline

N = int(input())
graph = []
shark = None

for i in range(N):
  temp = list(map(int,input().split()))
  graph.append(temp)
  for j in range(N):
    if temp[j] == 9:
      shark = (i,j,2,0)
      graph[i][j] = 0

res = 0
while True:
  t = bfs()
  if t == False:
    break
  res += t

print(res)