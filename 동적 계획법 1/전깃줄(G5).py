import sys

input = sys.stdin.readline

N = int(input())
edges = [list(map(int,input().split())) for _ in range(N)]
edges.sort()

dp = [1] * N

for i in range(1,N):
    t1 = 0
    for j in range(i):
        if edges[j][1] < edges[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N-max(dp))