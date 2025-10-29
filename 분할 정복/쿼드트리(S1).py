import sys

def solved(n,x,y):
  if n == 1:
    if graph[x][y] == 0:
      return "0"
    elif graph[x][y] == 1:
      return "1"
  
  a1 = solved(n//2, x, y)
  a2 = solved(n//2, x, y+n//2)
  a3 = solved(n//2, x+n//2, y)
  a4 = solved(n//2, x+n//2, y+n//2)

  if a1 == a2 == a3 == a4 == "1":
    return "1"
  elif a1 == a2 == a3 == a4 == "0":
    return "0"
  else:
    return f"({a1}{a2}{a3}{a4})"


N = int(input())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
print(solved(N,0,0))
