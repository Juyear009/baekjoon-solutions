T = int(input())

for i in range(T):
  k = int(input())
  n = int(input())
  house = [[0 for _ in range(n)] for _ in range(k+1)]
  house[0] = [i for i in range(1,n+1)]
  for i in range(1,k+1):
    for j in range(n):
      house[i][j] = sum(house[i-1][:j+1])
  print(house[k][n-1])