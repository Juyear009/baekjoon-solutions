import sys
from collections import deque

def bfs(sx,sy):
  count = 1
  queue = deque([[sx,sy]])
  visitedZero.add((sx,sy))
  visitedOne = set()
  d = [(0,1),(0,-1),(1,0),(-1,0)]
  temp = []
  while queue:
    x,y = queue.popleft()
    for dx,dy in d:
      nx = x + dx
      ny = y + dy
      if 0 <= nx < N and 0 <= ny < M:
        if (nx,ny) not in visitedZero and graph[nx][ny] == "0":
          queue.append([nx,ny])
          visitedZero.add((nx,ny))
          count = (count + 1) % 10
        elif (nx,ny) not in visitedOne and graph[nx][ny] == "1":
          temp.append([nx,ny])
          visitedOne.add((nx,ny))
  
  for x,y in temp:
    answer[x][y] = (answer[x][y] + count) % 10

input = sys.stdin.readline

N,M = map(int,input().split())
graph = [input() for _ in range(N)]
answer = [[1] * M for _ in range(N)]

visitedZero = set()
for i in range(N):
  for j in range(M):
    if graph[i][j] == "0" and (i,j) not in visitedZero:
      bfs(i,j)

for i in range(N):
  for j in range(M):
    if graph[i][j] == "0":
      print("0",end="")
    else:
      print(answer[i][j],end="")
  print()
