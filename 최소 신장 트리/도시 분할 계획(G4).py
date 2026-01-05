import sys
import heapq

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
parent = [i for i in range(N+1)]
edges = []
total = 0
for _ in range(M):
  a,b,c = map(int,input().split())
  edges.append((c,a,b))

edges.sort()
mst = 0
cnt = 0

for c,a,b in edges:
  if union(a,b):
    mst += c
    cnt += 1
    if cnt == N-1:
      mst -= c
      break

print(mst)