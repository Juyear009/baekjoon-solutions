import sys
from collections import deque

def solution():
  queue = deque(starts)
  while queue:
    node = queue.popleft()
    res.append(str(node))
    if graph[node]:
      for newNode in graph[node]:
        indegree[newNode] -= 1
        if indegree[newNode] == 0:
          queue.append(newNode)
      


input = sys.stdin.readline

N,M = map(int,input().split())
indegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
  t = list(map(int,input().split()))
  for i in range(2,len(t)):
    indegree[t[i]] += 1
    graph[t[i-1]].append(t[i])

starts = []
for i in range(1,len(indegree)):
  if indegree[i] == 0:
    starts.append(i)

res = []
solution()
if len(res) == N:
  print(" ".join(res))
else:
  print(0)