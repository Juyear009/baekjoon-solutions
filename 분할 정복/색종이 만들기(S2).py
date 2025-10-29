import sys

def solved(n,x,y):
  if n == 1:
    if graph[x][y] == 1:
      return (0,1)
    elif graph[x][y] == 0:
      return (1,0)
  
  a1 = solved(n//2,x,y)
  a2 = solved(n//2,x+n//2,y)
  a3 = solved(n//2,x,y+n//2)
  a4 = solved(n//2,x+n//2,y+n//2)

  total_white = a1[0] + a2[0] + a3[0] + a4[0]
  total_blue = a1[1] + a2[1] + a3[1] + a4[1]

  if total_white == 4 and total_blue == 0:
    return (1,0)
  elif total_white == 0 and total_blue == 4:
    return(0,1)
  else:
    return(total_white,total_blue)


N = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white, blue = solved(N,0,0)

print(white)
print(blue)