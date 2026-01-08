from collections import deque
import sys
input = sys.stdin.readline

def solution():
    t = int(input())
    for _ in range(t):
        n = int(input())
        last = list(map(int, input().split()))
        graph = [[False]*(n+1) for _ in range(n+1)]
        indeg = [0]*(n+1)

        for i in range(n):
            for j in range(i+1, n):
                u, v = last[i], last[j]
                graph[u][v] = True
                indeg[v] += 1

        m = int(input())
        for _ in range(m):
            a, b = map(int, input().split())
            if graph[a][b]:
                graph[a][b] = False
                graph[b][a] = True
                indeg[b] -= 1
                indeg[a] += 1
            else:
                graph[b][a] = False
                graph[a][b] = True
                indeg[a] -= 1
                indeg[b] += 1

        q = deque()
        for i in range(1, n+1):
            if indeg[i] == 0:
                q.append(i)

        result = []
        uncertain = False

        for _ in range(n):
            if not q:
                print("IMPOSSIBLE")
                break
            if len(q) > 1:
                uncertain = True

            cur = q.popleft()
            result.append(cur)

            for nxt in range(1, n+1):
                if graph[cur][nxt]:
                    indeg[nxt] -= 1
                    if indeg[nxt] == 0:
                        q.append(nxt)
        else:
            if uncertain:
                print("?")
            else:
                print(*result)

solution()