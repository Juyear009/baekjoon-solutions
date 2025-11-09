import sys
from collections import deque


def BFS():
  queue = deque([1])
  visited = set({1})
  cnt = 0
  while queue:
    node = queue.popleft()
    if node in graph:
      for i in graph[node]:
        if i not in visited:
          cnt += 1
          queue.append(i)
          visited.add(i)
  return cnt


input = sys.stdin.readline

N = int(input())
E = int(input())

graph = {}

for _ in range(E):
  u,v = map(int,input().split())
  graph.setdefault(u,[]).append(v)
  graph.setdefault(v,[]).append(u)

print(BFS())