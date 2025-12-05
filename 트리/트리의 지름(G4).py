import sys
from collections import deque

def bfs(s):
    queue = deque([s])
    dist = [-1] * (N+1)
    dist[s] = 0
    while queue:
        n = queue.popleft()
        for newN,w in tree[n]:
            if dist[newN] == -1:
                dist[newN] = dist[n] + w
                queue.append(newN)
    idx = dist.index(max(dist))
    return idx, dist[idx]

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

n,_ = bfs(1)
_,d = bfs(n)

print(d)