from collections import deque

def bfs(s):
  queue = deque([s])
  visited = [False] * N
  visited[s] = True
  while queue:
    node = queue.popleft()
    if graph[node]:
      for newNode in graph[node]:
        if not visited[newNode]:
          queue.append(newNode)
          visited[newNode] = True
  print(visited)
  return visited[E]

def solution():
  dist = [-float("INF") for _ in range(N)]
  dist[S] = benefit[S]
  for _ in range(N-1):
    check = False
    for u,v,w in edges:
      if dist[v] < dist[u] - w + benefit[v]:
        dist[v] = dist[u] - w + benefit[v]
        check = True
    if not check:
      break

  cycleNode = None
  for u,v,w in edges:
    if dist[v] < dist[u] - w + benefit[v]:
      dist[v] = dist[u] - w + benefit[v]
      cycleNode = v
  print(cycleNode)
  if cycleNode != None and bfs(cycleNode):
    print("Gee")
  elif dist[E] == -float("INF"):
    print("gg")
  else:
    print(dist[E])

N,S,E,M = map(int,input().split())
edges = []
graph = [[] for _ in range(N)]
for _ in range(M):
  u,v,w = map(int,input().split())
  edges.append((u,v,w))
  graph[u].append(v)
benefit = list(map(int,input().split()))

solution()