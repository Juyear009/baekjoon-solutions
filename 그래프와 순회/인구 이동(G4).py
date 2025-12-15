from collections import deque

def bfs(start):
  queue = deque([start])
  group = [start]
  d = [(1,0), (-1,0), (0,1), (0,-1)]
  while queue:
    x,y = queue.popleft()
    for dx, dy in d:
      newX = x + dx
      newY = y + dy
      if 0 <= newX < N and 0 <= newY < N:
        if L <= abs(graph[x][y] - graph[newX][newY]) <= R and (newX,newY) not in visited:
          visited.add((newX,newY))
          queue.append((newX,newY))
          group.append((newX,newY))
  if len(group) > 1:
    avg = sum(graph[x][y] for x,y in group) // len(group)
    for x,y in group:
      graph[x][y] = avg
    return True
  return False


N,L,R = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]
result = 0

while True:
  visited = set()
  check = False
  for i in range(N):
    for j in range(N):
      if (i,j) not in visited:
        visited.add((i,j))
        if bfs((i,j)):
          check = True
  if not check:
    break
  result += 1
print(result)