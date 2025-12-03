N = int(input())
nums = list(map(int,input().split()))

dp = [nums[0]]
pos = [0] * N

for i in range(1,N):
    if nums[i] > dp[-1]:
        dp.append(nums[i])
        pos[i] = len(dp) - 1
    else:
        left = 0
        right = len(dp) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[i] > dp[mid]:
                left = mid + 1
            elif nums[i] <= dp[mid]:
                right = mid - 1
        dp[left] = nums[i]
        pos[i] = left

print(len(dp))

res = []
t = len(dp) - 1
for i in range(N-1,-1,-1):
    if t == pos[i]:
        res.append(nums[i])
        t -= 1

for i in reversed(res):
    print(i, end=" ")