import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]*(n+1)
    for i in range(1, n+1):
        prefix[i] = prefix[i-1]+arr[i-1]
    INF = sys.maxsize
    dp = [[INF]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for cnt in range(n-1):
        for i in range(n-1-cnt):
            j = i+cnt+1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+prefix[j+1]-prefix[i])
    print(dp[0][n-1])
