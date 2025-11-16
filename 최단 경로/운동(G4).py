import sys

INF = 10**15
input = sys.stdin.readline

def floyd_warshall(n):
    dist = [[INF] * (n+1) for _ in range(n+1)]
    
    for _ in range(E):
      a, b, c = map(int, input().split())
      dist[a][b] = min(dist[a][b], c)

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                  dist[i][j] = dist[i][k] + dist[k][j]

    return dist

V,E = map(int,input().split())
dist = floyd_warshall(V)
print(dist)

result = INF
for i in range(1,V+1):
    result = min(result, dist[i][i])

if result == INF:
    print(-1)
else:
    print(result)
