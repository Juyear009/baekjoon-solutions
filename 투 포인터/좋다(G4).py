N = int(input())
nums = list(map(int, input().split()))
nums.sort()

result = 0

for i in range(N):
    target = nums[i]
    left = 0
    right = N-1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        s = nums[left] + nums[right]

        if s == target:
            result += 1
            break
        elif s < target:
            left += 1
        else:
            right -= 1

print(result)
