import sys
import heapq

def solution():
  global starts
  while starts:
    node = heapq.heappop(starts)
    res.append(str(node))
    if graph[node]:
      for newN in graph[node]:
        indegree[newN] -= 1
        if indegree[newN] == 0:
          heapq.heappush(starts,newN)



input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for _ in range(M):
  a,b = map(int,input().split())
  indegree[b] += 1
  graph[a].append(b)

starts = []
res = []
for i in range(1,len(indegree)):
  if indegree[i] == 0:
    heapq.heappush(starts,i)

solution()
print(" ".join(res))