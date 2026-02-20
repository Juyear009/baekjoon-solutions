import sys

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a,b):
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a

input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]

for i in range(N):
  t = list(map(int,input().split()))
  for j in range(N):
    if t[j] == 1:
      union(i+1,j+1)

city = list(map(int,input().split()))
root = find(city[0])
for i in city[1:]:
  if find(i) != root:
    print("NO")
    exit()

print("YES")