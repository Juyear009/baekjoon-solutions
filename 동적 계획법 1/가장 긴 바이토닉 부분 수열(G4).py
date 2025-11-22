N = int(input())
nums = list(map(int,input().split()))

dp = [[1,1] for _ in range(N)]

for i in range(1,N):
    t1 = 1
    t2 = 1
    for j in range(i):
        if nums[j] < nums[i]:
            t1 = max(t1, dp[j][0] + 1)
        if nums[j] > nums[i]:
            t2 = max(t2, dp[j][0] + 1, dp[j][1] + 1)
    dp[i][0] = t1
    dp[i][1] = t2

result = 0

for i in dp:
    if result < max(i):
        result = max(i)

print(result)

## chat GPT 피셜 정석 풀이
N = int(input())
nums = list(map(int, input().split()))

# 1. LIS 계산
lis = [1] * N
for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            lis[i] = max(lis[i], lis[j] + 1)

# 2. LDS 계산 (오른쪽 → 왼쪽)
lds = [1] * N
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if nums[j] < nums[i]:
            lds[i] = max(lds[i], lds[j] + 1)

# 3. LIS + LDS - 1
answer = 0
for i in range(N):
    answer = max(answer, lis[i] + lds[i] - 1)

print(answer)