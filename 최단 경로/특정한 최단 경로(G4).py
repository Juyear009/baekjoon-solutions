import sys
import heapq

def dijkstra(start, end):
  queue = []
  heapq.heappush(queue, (0,start))
  visited = set()
  while queue:
    w,v = heapq.heappop(queue)
    visited.add(v)
    if v == end:
      return w
    if graph[v]:
      for newV, newW in graph[v]:
        if newV not in visited:
          heapq.heappush(queue,(w+newW,newV))

input = sys.stdin.readline

N,E = map(int,input().split())

graph = [[] for _ in range(N+1)]

for i in range(E):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

v1,v2 = map(int,input().split())

result = 0
w1 = dijkstra(1,v1)
w2 = dijkstra(1,v2)
w3 = dijkstra(v1,v2)
w4 = dijkstra(v1,N)
w5 = dijkstra(v2,N)

if None in [w1,w2,w3,w4,w5]:
  print(-1)
else:
  print(min(w1 + w3 + w5, w2 + w3 + w4))
