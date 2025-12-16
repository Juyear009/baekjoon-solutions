import sys
import heapq

def dijkstra():
  queue = [(0,0,graph[0][0])]
  dist = [[float("inf") for _ in range(N)] for _ in range(N)]
  dist[0][0] = graph[0][0]
  d = [(0,1),(0,-1),(1,0),(-1,0)]
  while queue:
    x,y,p = heapq.heappop(queue)
    if x == N-1 and y == N-1:
      return p
    for dx, dy in d:
      newX = x + dx
      newY = y + dy
      if 0 <= newX < N and 0 <= newY < N:
        if p+graph[newX][newY] < dist[newX][newY]:
          dist[newX][newY] = p+graph[newX][newY]
          heapq.heappush(queue, (newX,newY,p+graph[newX][newY]))

input = sys.stdin.readline
case = 0
while True:
  case += 1
  N = int(input())
  if N == 0:
    break
  graph = [list(map(int,input().split())) for _ in range(N)]
  res = dijkstra()
  print(f"Problem {case}: {res}")
