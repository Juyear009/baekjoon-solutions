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

V,E = map(int,input().split())
edges = []
parent = [i for i in range(V+1)]
for _ in range(E):
  A,B,C = map(int,input().split())
  edges.append((C,A,B))

edges.sort()
res = 0
cnt = 0

for C,A,B in edges:
  if union(A,B):
    res += C
    cnt += 1
    if cnt == V-1:
      break

print(res)