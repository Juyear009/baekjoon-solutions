import sys
from collections import deque

def bfs():
  queue = deque([(0,1,0)])
  while queue:
    root,node,dist = queue.popleft()
    if root != 0:
      dp[node][1] = dp[node][1] + (dp[root][0]-dp[node][0]) * dist + dp[root][1]-dp[node][0] * dist - dp[node][1]
      dp[node][0] = N
    for child,newDist in tree[node]:
      if child != root:
        queue.append((node,child,newDist))

def dfs():
  stack = [(0,1,0,False)]
  while stack:
    root,node,total,check = stack.pop()
    if not check:
      stack.append((root,node,total,True))
      for child,dist in tree[node]:
        if child != root:
          stack.append((node,child,total+dist,False))
    if check:
      for child,dist in tree[node]:
        if child != root:
          dp[node][1] += dp[child][0] * dist + dp[child][1]
          dp[node][0] += dp[child][0]
      dp[node][0] += 1

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]


for _ in range(N-1):
  u,v,d = map(int,input().split())
  tree[u].append((v,d))
  tree[v].append((u,d))

dp = [[0,0] for _ in range(N+1)]
dfs()
bfs()
for n,r in dp[1:]:
  sys.stdout.write(str(r) + "\n")
