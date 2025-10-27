nums = list(input().split("-"))

result = 0

for i in range(len(nums)):
  add = list(map(int,nums[i].split("+")))
  sumNums = sum(add)
  if i == 0:
    result = sumNums
  else:
    result -= sumNums

print(result)