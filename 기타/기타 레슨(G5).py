def check(m):
    result = []
    t = 0
    if max(nums) > m:
        return False
    for i in nums:
        if t + i > m:
            result.append(t)
            t = 0
        t += i
    if t != 0:
        result.append(t)
    if len(result) > M:
        return False
    else:
        return True

def binary_search():
    left = 1
    right = sum(nums)
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left

N,M = map(int,input().split())
nums = list(map(int,input().split()))

print(binary_search())