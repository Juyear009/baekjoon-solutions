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
    size[a] += size[b]
    size[b] = 0

input = sys.stdin.readline

T = int(input())
for _ in range(T):
  F = int(input())
  parent = []
  size = []
  dic = {}
  for _ in range(F):
    a,b = input().split()
    if a not in dic:
      dic[a] = len(parent)
      parent.append(len(parent))
      size.append(1)
    if b not in dic:
      dic[b] = len(parent)
      parent.append(len(parent))
      size.append(1)
    union(dic[a], dic[b])
    root = parent[dic[a]]
    print(size[root])