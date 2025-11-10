import sys
import heapq

def dijkstra(K):
  heap = []
  heapq.heappush(heap,(0,K))
  result[K] = 0
  while heap:
    length, node = heapq.heappop(heap)
    if length > result[node]:
      continue
    if graph[node]:
      for v,w in graph[node]:
        if result[v] == "INF" or length + w < result[v]:
          result[v] = length+w
          heapq.heappush(heap,(length+w,v))


input = sys.stdin.readline

V,E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
result = ["INF"] * (V+1)

for _ in range(E):
  u,v,w = map(int,input().split())
  graph[u].append((v,w))

dijkstra(K)
for i in result[1:]:
  sys.stdout.write(str(i) + "\n")