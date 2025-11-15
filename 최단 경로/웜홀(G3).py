import sys

def solution():
    dist = [float('inf')] * (N+1)
    dist[1] = 0

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
            return True
    return False

input = sys.stdin.readline

T = int(input())

for i in range(T):
    N,M,W = map(int,input().split())
    edges = []
    
    for j in range(M):
        S,E,T = map(int,input().split())
        edges.append((S,E,T))
        edges.append((E,S,T))
    for j in range(W):
        S,E,T = map(int,input().split())
        edges.append((S,E,-T))
    if solution():
        print("YES")
    else:
        print("NO")