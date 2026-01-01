import sys

def dfs():
  stack = [(0,1,False)]
  while stack:
    parent,node,check = stack.pop()
    if not check:
      stack.append((parent,node,True))
      for child in tree[node]:
        if child != parent:
          stack.append((node,child,False))
    else:
      for child in tree[node]:
        if child != parent:
          dp[node][0] += max(dp[child])
          dp[node][1] += dp[child][0]
      dp[node][1] += people[node-1]


input = sys.stdin.readline

N = int(input())
people = list(map(int,input().split()))
tree = [[] for _ in range(N+1)]
dp = [[0,0] for _ in range(N+1)]

for _ in range(N-1):
  u,v = map(int,input().split())
  tree[u].append(v)
  tree[v].append(u)

dfs()
print(max(dp[1]))