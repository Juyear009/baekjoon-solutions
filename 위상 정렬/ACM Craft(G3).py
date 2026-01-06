import sys
import heapq

def solution():
  while starts:
    time,node = heapq.heappop(starts)
    if node == W:
      return time
    if graph[node]:
      for newNode in graph[node]:
        indegree[newNode] -= 1
        if indegree[newNode] == 0:
          heapq.heappush(starts,(time+times[newNode-1],newNode))


input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N,K = map(int,input().split())
  times = list(map(int,input().split()))
  indegree = [0 for _ in range(N+1)]
  graph = [[] for _ in range(N+1)]
  for _ in range(K):
    x,y = map(int,input().split())
    indegree[y] += 1
    graph[x].append(y)
  W = int(input())
  starts = []
  for i in range(1,N+1):
    if indegree[i] == 0:
      heapq.heappush(starts,(times[i-1],i))
  print(solution())