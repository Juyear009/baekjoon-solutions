import sys
import heapq

def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    dists = [float('inf')] * (n+1)
    dists[start] = 0
    while queue:
        d,v = heapq.heappop(queue)
        if dists[v] < d:
            continue
        if graph[v]:
            for newV, newD in graph[v]:
                if d + newD < dists[newV]:
                    dists[newV] = d + newD
                    heapq.heappush(queue, (d+newD, newV))
    return dists



input = sys.stdin.readline

T = int(input())

for i in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    result = []
    for j in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    gd = dijkstra(g)
    sd = dijkstra(s)
    hd = dijkstra(h)
    for j in range(t):
        end = int(input())
        path1 = sd[g] + gd[h] + hd[end]
        path2 = sd[h] + hd[g] + gd[end]
        minPath = min(path1, path2)
        if sd[end] != float('inf') and sd[end] == minPath:
            result.append(end)
    result.sort()
    for i in result:
        print(i,end=" ")
    print()