import sys

def solved():
  N, M, K = map(int,input().split())

  Black = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

  for i in range(1,N + 1):
    maps = list(sys.stdin.readline().rstrip())
    for j in range(1,M + 1):
      if (t1 == 1 and maps[i-1][j-1] == "W") or (t1 == 0 and maps[i-1][j-1] == "B"):
        Black[i][j] = Black[i-1][j] + Black[i][j-1] - Black[i-1][j-1]
      else:
        Black[i][j] = Black[i-1][j] + Black[i][j-1] - Black[i-1][j-1] + 1
      t1 ^= 1
      
  result = 10000000

  for i in range(N-K+1):
    for j in range(M-K+1):
      cnt = Black[i+K][j+K] - Black[i+K][j] - Black[i][j+K] + Black[i][j]
      result = min(cnt, K*K-cnt, result)

  return result


print(solved())