from itertools import combinations
from bisect import bisect_left, bisect_right

def combination(arr):
  sums = []
  for i in range(1,len(arr) + 1):
    for c in combinations(arr, i):
        sums.append(sum(c))
  return sums

N,S = map(int,input().split())
nums = list(map(int,input().split()))

left_sum = combination(nums[:N//2])
right_sum = combination(nums[N//2:])

left_sum.sort()
right_sum.sort()

p1 = 0
p2 = len(right_sum) - 1
result = 0


for lv in left_sum:
    target = S - lv
    l_idx = bisect_left(right_sum, target)
    r_idx = bisect_right(right_sum, target)
    result += r_idx - l_idx

result += left_sum.count(S)
result += right_sum.count(S)

print(result)
