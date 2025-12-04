V = int(input())

def dfs(s):
    stack = [s]
    dist = [-1] * (V+1)
    dist[s] = 0
    while stack:
        v = stack.pop()
        for newV,w in tree[v]:
            if dist[newV] == -1:
                dist[newV] = dist[v] + w
                stack.append(newV)

    return dist

tree = [[] for _ in range(V+1)]
for i in range(V):
    edges = list(map(int,input().split()))
    for j in range((len(edges)-2)//2):
        tree[edges[0]].append((edges[j*2+1],edges[j*2+2]))

t = dfs(1)
print(max(dfs(t.index(max(t)))))