import sys

def dfs(s):
  stack = [(s,0)]
  visited.add(s)
  while stack:
    cur, parent = stack.pop()
    if tree[cur]:
      for newN in tree[cur]:
        if newN not in visited:
          visited.add(newN)
          stack.append((newN,cur))
        elif newN != parent:
          return False
  return True

input = sys.stdin.readline
c = 0

while True:
  c += 1
  n,m = map(int,input().split())
  if n == 0 and m == 0:
    break

  tree = [[] for _ in range(n+1)]
  for i in range(m):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

  visited = set()
  result = 0
  for i in range(1,n+1):
    if i not in visited:
      if dfs(i):
        result += 1
  
  if result > 1:
    print(f"Case {c}: A forest of {result} trees.")
  elif result == 1:
    print(f"Case {c}: There is one tree.")
  elif result == 0:
    print(f"Case {c}: No trees.")