H,W = map(int,input().split())
heights = list(map(int,input().split()))


res = 0
for y in range(1,H+1):
  temp = 0
  wall = False
  for x in range(W):
    if heights[x] >= y:
      if not wall:
        wall = True
      elif wall:
        res += temp
        temp = 0
    elif heights[x] < y:
      if wall:
        temp += 1

print(res)