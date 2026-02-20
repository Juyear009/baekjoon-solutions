import sys

def find(x):
  if x != parent[x]:
    parent[x] = find(parent[x])
  return parent[x]

def union(x,y):
  a = find(x)
  b = find(y)
  if a != b:
    parent[b] = a

input = sys.stdin.readline

G = int(input())
P = int(input())

parent = [i for i in range(G+1)]
cnt = 0

for i in range(P):
  g = int(input())
  p = find(g)
  if p != 0:
    union(p-1,p)
    cnt += 1
  else:
    break

print(parent,cnt)