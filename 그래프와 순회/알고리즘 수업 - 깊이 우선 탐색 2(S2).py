import sys

def dfs():
    visited = set({})
    stack = [R]
    level = 0
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        level += 1
        result[node-1] = level
        if node not in graph:
            continue
        for i in graph[node]:
            stack.append(i)


input = sys.stdin.readline
N,M,R = map(int,input().split())
graph = {}

for i in range(M):
    u,v = map(int,input().split())
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]
    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]

for i in graph:
    graph[i].sort()

result = [0 for _ in range(N)]

dfs()

for i in result:
    sys.stdout.write(str(i) + "\n")