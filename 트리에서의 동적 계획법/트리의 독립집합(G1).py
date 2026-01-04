import sys
from collections import deque

def dfs():
  stack = [(0,1,False)]
  while stack:
    root,node,check = stack.pop()
    if not check:
      stack.append((root,node,True))
      for child in tree[node]:
        if child != root:
          stack.append((node,child,False))
    else:
      for child in tree[node]:
        if child != root:
          dp[node][1] += dp[child][0]
          dp[node][0] += max(dp[child])
      dp[node][1] += weights[node-1]

def bfs(s):
  queue = deque([(0,1,s)])
  visited = set()
  visited.add(1)
  while queue:
    root,node,select = queue.popleft()
    if select == 1:
      res.append(node)
    for child in tree[node]:
      if child != root:
        if select == 1:
          queue.append((node,child,0))
        else:
          if dp[child][1] >= dp[child][0]:
            queue.append((node,child,1))
          else:
            queue.append((node,child,0))


input = sys.stdin.readline

n = int(input())
weights = list(map(int,input().split()))
tree = [[] for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]
for _ in range(n-1):
  a,b = map(int,input().split())
  tree[a].append(b)
  tree[b].append(a)

dfs()
res = []
if dp[1][1] >= dp[1][0]:
  bfs(1)
else:
  bfs(0)

res.sort()
print(max(dp[1]))
for n in res:
  print(n, end=" ")