import sys

sys.setrecursionlimit(10**6)

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

N,M = map(int,input().split())
edges = []
parent = [i for i in range(N)]
pos = []

for i in range(N):
  x,y = map(int,input().split())
  pos.append((x,y))

for i in range(M):
  a,b = map(int,input().split())
  union(a-1,b-1)

for i in range(N-1):
  x,y = pos[i]
  for j in range(i+1,N):
    x1,y1 = pos[j]
    length = (abs(x-x1)**2 + abs(y-y1)**2)**0.5
    edges.append((length,i,j))

edges.sort()
mst = 0
cnt = 0

for c,a,b in edges:
  if union(a,b):
    mst += c
    cnt += 1
    if cnt == N-1:
      break
  
print(f"{mst:.2f}")