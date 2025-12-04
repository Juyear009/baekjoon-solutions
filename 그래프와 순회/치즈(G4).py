import sys
from collections import deque

def bfs():
    queue = deque([(0,0)])
    visited = set((0,0))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    result = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if 0 <= newX < N and 0 <= newY < M and (newX,newY) not in visited:
                visited.add((newX,newY))
                if graph[newX][newY] == 1 and (newX,newY) not in cheese:
                    cheese.add((newX,newY))
                    result += 1
                else:
                    queue.append((newX,newY))
    return result

input = sys.stdin.readline
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
cheese = set()
cnt = []

while True:
    cheeseCnt = bfs()
    if cheeseCnt == 0:
        break
    cnt.append(cheeseCnt)

print(len(cnt))
print(cnt[-1])