import sys
from collections import deque

def solution(r,c,d):
  queue = deque([(r,c,d)])
  visited = set()
  res = 0
  dxdy = [(-1,0),(0,1),(1,0),(0,-1)]
  while queue:
    x,y,d = queue.popleft()
    if (x,y) not in visited:
      visited.add((x,y))
      res += 1
    allClean = True
    for dx,dy in dxdy:
      newX = x + dx
      newY = y + dy
      if 0 <= newX < N and 0 <= newY < M:
        if graph[newX][newY] != 1 and (newX,newY) not in visited:
          allClean = False
          break
    
    if allClean:
      t = (d+2)%4
      if graph[x+dxdy[t][0]][y+dxdy[t][1]] == 0:
        queue.append((x+dxdy[t][0],y+dxdy[t][1],d))
      else:
        return res
    elif not allClean:
      d -= 1
      if d == -1:
        d = 3
      if graph[x+dxdy[d][0]][y+dxdy[d][1]] == 0 and (x+dxdy[d][0],y+dxdy[d][1]) not in visited:
        queue.append((x+dxdy[d][0],y+dxdy[d][1],d))
      else:
        queue.append((x,y,d))


input = sys.stdin.readline

N,M = map(int,input().split())
r,c,d = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

print(solution(r,c,d))