import sys

def dfs():
  stack = [(0,R,False)]
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
          dp[node] += dp[child]
      dp[node] += 1


input = sys.stdin.readline

N,R,Q = map(int,input().split())
tree = [[] for _ in range(N+1)]
dp = [0 for _ in range(N+1)]

for _ in range(N-1):
  U,V = map(int,input().split())
  tree[U].append(V)
  tree[V].append(U)

dfs()

for _ in range(Q):
  print(dp[int(input())])