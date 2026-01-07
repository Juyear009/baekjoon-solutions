import heapq

def dijkstra():
  queue = []
  heapq.heappush(queue,(0,0,0))
  d = [(0,1),(0,-1),(1,0),(-1,0)]
  while queue:
    c,x,y = heapq.heappop(queue)
    for dx,dy in d:
      newX = x + dx
      newY = y + dy
      if 0 <= newX < N and 0 <= newY < M:
        if graph[newX][newY] == 1:
          if dist[newX][newY] > c + 1:
            heapq.heappush(queue,(c+1,newX,newY))
            dist[newX][newY] = c + 1
        else:
          if dist[newX][newY] > c:
            heapq.heappush(queue,(c,newX,newY))
            dist[newX][newY] = c


M,N = map(int,input().split())
graph = [[] for _ in range(N)]
for i in range(N):
  t = input()
  for j in t:
    graph[i].append(int(j))

dist = [[float('INF') for _ in range(M)] for _ in range(N)]
dist[0][0] = 0
dijkstra()
print(dist[-1][-1])