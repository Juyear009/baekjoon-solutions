import math

M = int(input())
N = int(input())

if M == 1:
  nums = [i for i in range(M+1,N+1)]
else:
  nums = [i for i in range(M,N+1)]

for i in range(2,int(math.sqrt(N))+1):
  for j in range(len(nums)):
    if nums[j] % i == 0 and nums[j] != i:
      nums[j] = 0

sum = 0
minNum = 10001
for i in nums:
  if i != 0:
    sum += i
    if minNum > i:
      minNum = i

if sum == 0:
  print(-1)
else:
  print(sum)
  print(minNum)