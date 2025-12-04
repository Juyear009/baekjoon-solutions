from collections import deque
import sys

def bfs(wall):
    queue = deque(virus)
    visited = set()
    result = -len(queue)
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while queue:
        x,y = queue.popleft()
        result += 1
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if 0 <= newX < N and 0 <= newY < M and graph[newX][newY] == 0 and (newX,newY) not in wall:
                if (newX,newY) not in visited:
                    queue.append((newX,newY))
                    visited.add((newX,newY))
    return result

input = sys.stdin.readline
N,M = map(int,input().split())

graph = []
zero = []
virus = []

for i in range(N):
    temp = list(map(int,input().split()))
    graph.append(temp)
    for j in range(len(temp)):
        if temp[j] == 0:
            zero.append((i,j))
        elif temp[j] == 2:
            virus.append((i,j))

result = 0

for i in range(len(zero)-2):
    for j in range(i+1,len(zero)-1):
        for k in range(j+1,len(zero)):
            res = bfs([zero[i],zero[j],zero[k]])
            if len(zero) - res - 3 > result:
                result = len(zero) - res - 3

print(result)
