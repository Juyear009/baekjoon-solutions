import sys

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(x,y):
  a = find(x)
  b = find(y)
  if a != b:
    parent[b] = a
    return True
  return False

input = sys.stdin.readline

while True:
  m,n = map(int,input().split())
  if m == 0 and n == 0:
    break
  parent = [i for i in range(m)]
  edges = []
  total = 0
  for _ in range(n):
    x,y,z = map(int,input().split())
    edges.append((z,x,y))
    total += z

  edges.sort()
  mst = 0
  cnt = 0
  check = True
  for c,x,y in edges:
    if union(x,y) and check:
      mst += c
      cnt += 1
      if cnt == m-1:
        check = False

  print(total-mst)