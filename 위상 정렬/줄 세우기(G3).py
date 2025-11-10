import sys
from collections import deque

def topology(S,init):
  queue = deque(init)
  result = []
  while queue:
    node = queue.popleft()
    result.append(str(node))
    if graph[node]:
      for i in graph[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
          queue.append(i)
  return list(reversed(result))


input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
starts = []

for i in range(M):
  A,B = map(int,input().split())
  graph[B].append(A)
  indegree[A] += 1

for i in range(1,len(indegree)):
  if indegree[i] == 0:
    starts.append(i)

result = topology(i,starts)
print(" ".join(result), end=" ")

