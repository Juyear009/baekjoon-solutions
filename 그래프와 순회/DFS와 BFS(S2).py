import sys
from collections import deque

def dfs():
    stack = [V]
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        dfs_result.append(str(node))
        if node in graph:
            for i in range(len(graph[node])-1,-1,-1):
                stack.append(graph[node][i])

def bfs():
    queue = deque([V])
    visited = set()
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        bfs_result.append(str(node))
        if node in graph:
            for i in graph[node]:
                queue.append(i)


input = sys.stdin.readline

N,M,V = map(int,input().split())
graph = {}

for i in range(M):
    n1,n2 = map(int,input().split())
    if n1 in graph:
        graph[n1].append(n2)
    else:
        graph[n1] = [n2]
    if n2 in graph:
        graph[n2].append(n1)
    else:
        graph[n2] = [n1]

for i in graph:
    graph[i].sort()

dfs_result = []
bfs_result = []

dfs()
bfs()

print(" ".join(dfs_result))
print(" ".join(bfs_result))