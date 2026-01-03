import math

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

n = int(input())
edges = []
stars = []
parent = [i for i in range(n)]

for i in range(n):
  x,y = map(float,input().split())
  stars.append((x,y))
  for j in range(i):
    x1,y1 = stars[j]
    length = math.sqrt(abs(x-x1)**2 + abs(y-y1)**2)
    edges.append((length,i,j))

edges.sort()
mst = 0
cnt = 0

for c,a,b in edges:
  if union(a,b):
    mst += c
    cnt += 1
    if cnt == n-1:
      break

print(f"{mst:.2f}")