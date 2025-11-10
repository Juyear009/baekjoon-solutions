import sys
from collections import deque

def bfs(s):
  queue = deque([s])
  while queue:
    node = queue.popleft()
    if graph[node]:
      for i in graph[node]:
        if i not in visited:
          queue.append(i)
          visited.add(i)

input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
  u,v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)

result = 0
visited = set()

for i in range(1,N+1):
  if i not in visited:
    visited.add(i)
    result += 1
    bfs(i)

print(result)