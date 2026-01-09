import heapq

def bfs(s):
  queue = []
  heapq.heappush(queue,(0,s))
  dist = [float('inf')] * (n+1)
  dist[s] = 0
  while queue:
    d,node = heapq.heappop(queue)
    if graph[node]:
      for newNode,newD in graph[node]:
        if dist[newNode] > d + newD and d + newD <= m:
          heapq.heappush(queue,(d+newD,newNode))
          dist[newNode] = d + newD

  res = 0
  for i in range(1,n+1):
    if dist[i] <= m:
      res += t[i-1]
  return res


n,m,r = map(int,input().split())
t = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
  a,b,l = map(int,input().split())
  graph[a].append((b,l))
  graph[b].append((a,l))

res = 0
for i in range(1,n+1):
  a = bfs(i)
  if res < a:
    res = a

print(res)