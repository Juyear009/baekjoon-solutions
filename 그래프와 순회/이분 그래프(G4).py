import sys
from collections import deque

def bfs():
  queue = deque([(1,0)])
  visited = set({1})
  groups = [set(),set()]
  while queue:
    node,group = queue.popleft()
    if node in graph:
      for i in graph[node]:
        if i not in visited:
          queue.append((i,(group+1)%2))
          visited.add(i)
          groups[(group+1)%2].add(i)
        elif i in groups[group]:
            return "NO"
    if len(queue) == 0 and len(visited) != V:
      maxNode = max(visited)
      queue.append((maxNode+1,0))
      visited.add(maxNode+1)
  return "YES"


input = sys.stdin.readline

K = int(input())

for i in range(K):
  V,E = map(int,input().split())
  graph = {}
  for _ in range(E):
    u,v = map(int,input().split())
    graph.setdefault(u,[]).append(v)
    graph.setdefault(v,[]).append(u)

  print(bfs())