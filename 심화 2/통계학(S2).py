import sys
import math

N = int(input())
nums = []
dic = {}
maxNum = -4001
minNum = 4001
sumNum = 0

for i in range(N):
  num = int(sys.stdin.readline().strip())
  nums.append(num)
  sumNum += num
  if num in dic:
    dic[num] += 1
  elif num not in dic:
    dic[num] = 1
  if maxNum < num:
    maxNum = num
  if minNum > num:
    minNum = num

nums.sort()
mostCnt = max(dic.values())
temp = []

for i in dic:
  if dic[i] == mostCnt:
    temp.append(i)

print(round(sumNum / N))
print(nums[N//2])
if len(temp) == 1:
  print(temp[0])
else:
  temp.sort()
  print(temp[1])
print(maxNum - minNum)