def check(m):
    result = []
    t = 0
    for i in nums:
        if t + i > m:
            result.append(t)
            t = i
        else:
            t += i

def binary_search():
    left = 1
    right = sum(nums)
    while left <= right:
        mid = (left + right) // 2
        i

N,M = map(int,input().split())

nums = list(map(int,input().split()))