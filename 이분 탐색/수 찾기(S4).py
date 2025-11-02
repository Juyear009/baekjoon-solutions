def binary_search(nums, target):
  left, right = 0, len(nums) - 1
  while left <= right:
    mid = (left + right) // 2
    if nums[mid] < target:
      left = mid + 1
    elif nums[mid] > target:
      right = mid - 1
    elif nums[mid] == target:
      return 1
  return 0

N = int(input())
nums = list(map(int,input().split()))
M = int(input())
findNums = list(map(int,input().split()))

nums.sort()

for i in findNums:
  print(binary_search(nums,i))