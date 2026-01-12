import heapq
import sys

def dijkstra(s,e):
  queue = []
  heapq.heappush(queue,(0,s))
  dist = [float('inf')] * (n+1)
  dist[s] = 0
  parent = [0 for _ in range(n+1)]
  while queue:
    curDist,curNode = heapq.heappop(queue)
    if curDist > dist[curNode]:
      continue # 기존 거리가 더 짧은 것은 바로 패스
    if graph[curNode]:
      for newNode,newDist in graph[curNode]:
        if dist[newNode] > curDist + newDist:
          dist[newNode] = curDist + newDist
          parent[newNode] = curNode
          heapq.heappush(queue,(curDist+newDist,newNode))
  print(dist[e])
  res = [e]
  while True:
    t = parent[e]
    if t == 0:
      break
    res.append(t)
    e = t
  print(len(res))
  for i in range(len(res)-1,-1,-1):
    print(res[i],end=" ")

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  u,v,w = map(int,input().split())
  graph[u].append((v,w))

s,e = map(int,input().split())
dijkstra(s,e)