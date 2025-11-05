def inverterPos(num):
  y = (num - 1) // 10
  x = (num - 1) % 10
  if y % 2 == 1:
      x = 9 - x
  return (x,y)

def dfs():
  s = [(0,0,0)]
  visit[0][0] = 0
  dice = [1,2,3,4,5,6]
  result = 100001
  while s:
    x,y,l = s.pop(-1)
    if x == 0 and y == 9:
      if l < result:
        result = l
        continue
    for i in dice:
      newX = x
      newY = y
      newL = l + 1
      if y % 2 == 0:
        newX += i
        if newX >= 10:
          newX = 19 - newX
          newY += 1
      else:
        newX -= i
        if newX < 0:
          newX = abs(newX) - 1
          newY += 1
      if (newX,newY) in ledders:
        newX,newY = ledders[(newX,newY)]
      elif (newX,newY) in snakes:
        newX,newY = snakes[(newX,newY)]
      if newY <= 9 and visit[newY][newX] > newL:
        s.append((newX,newY,newL))
        visit[newY][newX] = newL
  return result
      

N, M = map(int,input().split())

ledders = {}
snakes = {}
visit = [[10000 for _ in range(10)] for _ in range(10)]

for i in range(N):
  p1, p2 = map(int,input().split())
  ledders[inverterPos(p1)] = inverterPos(p2)

for i in range(M):
  p1, p2 = map(int,input().split())
  snakes[inverterPos(p1)] = inverterPos(p2)

print(dfs())