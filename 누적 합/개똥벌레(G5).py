import sys

input = sys.stdin.readline

N,H = map(int,input().split())
sum_nums = [0] * (H)

for i in range(N):
  t = int(input())
  if i % 2 == 0:
    sum_nums[0] += 1
    sum_nums[t] -= 1
  else:
    sum_nums[H-t] += 1

for i in range(1,H):
  sum_nums[i] = sum_nums[i-1] + sum_nums[i]

res = min(sum_nums)
print(res,sum_nums.count(res))
