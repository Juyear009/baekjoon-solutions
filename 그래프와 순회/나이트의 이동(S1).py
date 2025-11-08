import sys
from collections import deque

def bfs():
    queue = deque([(cx,cy,0)])
    dx = [1,1,2,2,-1,-1,-2,-2]
    dy = [2,-2,1,-1,2,-2,1,-1]
    visited = set({(cx,cy)})
    while queue:
        x,y,cnt = queue.popleft()
        if x == fx and y == fy:
            return cnt
        for i in range(8):
            newX = x + dx[i]
            newY = y + dy[i]
            if 0 <= newX < l and 0 <= newY < l:
                if (newX,newY) not in visited:
                    queue.append((newX,newY,cnt+1))
                    visited.add((newX,newY))

input = sys.stdin.readline

T = int(input())

for i in range(T):
    l = int(input())
    cx,cy = map(int,input().split())
    fx,fy = map(int,input().split())
    print(bfs())
