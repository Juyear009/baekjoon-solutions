import sys

def dfs():
  stack = [(1,0,False)]
  while stack:
    node,parent,check = stack.pop()
    if not check:
      stack.append((node,parent,True))
      if tree[node]:
        for newNode in tree[node]:
          if newNode != parent:
            stack.append((newNode,node,False))
    else:
      for child in tree[node]:
        if child != parent:
          dp[node][0] += dp[child][1]
          dp[node][1] += min(dp[child][0], dp[child][1])
      dp[node][1] += 1


input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
dp = [[0,0] for _ in range(N+1)]

for _ in range(N-1):
  u,v = map(int,input().split())
  tree[u].append(v)
  tree[v].append(u)

dfs()
print(min(dp[1]))

