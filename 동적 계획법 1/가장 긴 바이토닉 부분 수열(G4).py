N = int(input())
nums = list(map(int,input().split()))

dp = [[1,1] for _ in range(N)]

for i in range(1,N):
    t1 = 1
    t2 = 1
    for j in range(i):
        if nums[j] < nums[i]:
            if t1 < dp[j][0] + 1:
                t1 = dp[j][0] + 1
        if nums[j] > nums[i]:
            t2 = max(dp[j][0] + 1, dp[j][1] + 1)
    dp[i][0] = t1
    dp[i][1] = t2

result = 0

for i in dp:
    if result < max(i):
        result = max(i)

print(result)