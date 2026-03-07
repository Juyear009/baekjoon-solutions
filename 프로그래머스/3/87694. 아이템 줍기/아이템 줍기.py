from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    def bfs():
        nonlocal answer
        queue = deque([[characterX,characterY,0]])
        visited = set({(characterX,characterY)})
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            x,y,d = queue.popleft()
            if itemX == x and itemY == y:
                answer = min(answer,d)
            for dx,dy in direction:
                nx = x + dx
                ny = y + dy
                if 0 <= nx <= 100 and 0 <= ny <= 100:
                    if (nx,ny) not in visited and graph[ny][nx] == 1:
                        queue.append([nx,ny,d+1])
                        visited.add((nx,ny))
                        
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
            
    answer = float("inf")
    graph = [[0] * 101 for _ in range(101)]
    for x1,y1,x2,y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        for y in range(y1,y2+1):
            for x in range(x1,x2+1):
                graph[y][x] = 1
                
    for x1,y1,x2,y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        for y in range(y1,y2+1):
            for x in range(x1,x2+1):
                if y not in [y1,y2] and x not in [x1,x2]:
                    graph[y][x] = 0
        
    bfs()
    return answer // 2