import sys
input = sys.stdin.readline
INF = 10**9

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j][d]
dp = [[[INF]*3 for _ in range(m)] for _ in range(n)]

# 초기값
for j in range(m):
    for d in range(3):
        dp[0][j][d] = a[0][j]

move = [-1, 0, 1]

for i in range(1, n):
    for j in range(m):
        for d in range(3):
            pj = j - move[d]
            if 0 <= pj < m:
                for prev_d in range(3):
                    if prev_d != d:
                        dp[i][j][d] = min(
                            dp[i][j][d],
                            dp[i-1][pj][prev_d] + a[i][j]
                        )

ans = INF
for j in range(m):
    for d in range(3):
        ans = min(ans, dp[n-1][j][d])

print(ans)
