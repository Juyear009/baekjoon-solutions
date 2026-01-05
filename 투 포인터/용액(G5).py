N = int(input())
nums = list(map(int,input().split()))

p1 = 0
p2 = len(nums)-1

t = 10**10
res = [0,0]

while p1 < p2:
  s = nums[p1] + nums[p2]
  if abs(s) <= t:
    t = abs(s)
    res[0] = str(nums[p1])
    res[1] = str(nums[p2])
  if s > 0:
    p2 -= 1
  elif s < 0:
    p1 += 1
  elif s == 0:
    break

print(" ".join(res))