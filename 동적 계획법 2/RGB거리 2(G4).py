import sys

input = sys.stdin.readline

N = int(input())
INF = 10**9
answer = INF
p = [list(map(int,input().split())) for _ in range(N)]


for s in range(3):
  dp = [[INF]*3 for _ in range(N)]
  dp[0][s] = p[0][s]

  for i in range(1,N):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + p[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + p[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + p[i][2]

  for e in range(3):
    if e != s:
      answer = min(answer, dp[N-1][e])

print(answer)