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

input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n)]

for i in range(m):
  a,b = map(int,input().split())
  if find(a) == find(b):
    print(i+1)
    exit()
  union(a,b)
print(0)