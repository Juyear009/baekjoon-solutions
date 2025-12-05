from collections import deque

def bfs(s):
  queue = deque([s])
  visited = set()
  visited.add(s)
  res = 0
  while queue:
    n = queue.popleft()
    if tree[n]:
      for newN in tree[n]:
        if newN not in visited:
          queue.append(newN)
          visited.add(newN)
    else:
      res += 1
  return res

N = int(input())
parent = list(map(int,input().split()))
deleteNode = int(input())
startNode = -1
tree = [[] for _ in range(N)]

for i in range(N):
  if parent[i] == -1:
    startNode = i
  else:
    tree[parent[i]].append(i)

if parent[deleteNode] != -1:
    tree[parent[deleteNode]].remove(deleteNode)

if deleteNode == startNode:
  print(0)
else:
  print(bfs(startNode))