## 이분탐색 LIS는 매우 자주 쓰이는 핵심 알고리즘 중 하나임.
## 증가하는 부분 수열을 NlogN 시간복잡도로 찾을 수 있는 알고리즘임.
## DP의 경우에도 N제곱의 시간복잡도가 필요함.

def solution():
  result = [nums[0]]
  for i in nums[1:]:
    if i > result[-1]:
      result.append(i)
    else:
      left = 0
      right = len(result) - 1
      while left <= right:
        mid = (left + right) // 2
        if i <= result[mid]:
          right = mid - 1
        elif i > result[mid]:
          left = mid + 1
      if result[left] > i:
        result[left] = i
  return len(result)

N = int(input())
nums = list(map(int,input().split()))

print(solution())