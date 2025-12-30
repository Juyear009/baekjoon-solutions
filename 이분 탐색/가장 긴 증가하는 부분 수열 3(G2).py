def solution():
  res = [nums[0]]
  for i in range(1,N):
    if res[-1] < nums[i]:
      res.append(nums[i])
    else:
      left = 0
      right = len(res)-1
      while left <= right:
        mid = (left+right)//2
        if res[mid] >= nums[i]:
          right = mid - 1
        elif res[mid] < nums[i]:
          left = mid + 1
      if res[left] > nums[i]:
        res[left] = nums[i]
      
  return len(res)

N = int(input())
nums = list(map(int,input().split()))

print(solution())