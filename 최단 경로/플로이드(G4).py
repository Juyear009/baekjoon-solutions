import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
  dist[i][i] = 0

for i in range(m):
  a,b,c = map(int,input().split())
  dist[a][b] = min(dist[a][b], c)

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      if dist[i][j] > dist[i][k] + dist[k][j]:
        dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1,n+1):
  for j in range(1,n+1):
    if dist[i][j] == float('inf'):
      sys.stdout.write("0 ")
    else:
      sys.stdout.write(str(dist[i][j]) + " ")
  sys.stdout.write("\n")