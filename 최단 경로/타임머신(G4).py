import sys

def solution():
    for _ in range(N-1):
        check = False
        for u,v,w in edges:
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                check = True
        if not check:
            break

    for u,v,w in edges:
        if dist[u] != float('inf') and dist[v] > dist[u] + w:
            return False
    return True

input = sys.stdin.readline

N,M = map(int,input().split())
edges = []
dist = [float('inf')] *  (N+1)
dist[1] = 0

for i in range(M):
    A,B,C = map(int,input().split())
    edges.append((A,B,C))

if solution():
    for i in dist[2:]:
        if i == float('inf'):
            print(-1)
        else:
            print(i)
else:
    print(-1)