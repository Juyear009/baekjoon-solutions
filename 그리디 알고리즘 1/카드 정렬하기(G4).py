import sys
import heapq

input = sys.stdin.readline

N = int(input())
nums = []

for i in range(N):
  heapq.heappush(nums,int(input()))

result = 0

while len(nums) > 1:
  print(nums)
  c1 = heapq.heappop(nums)
  c2 = heapq.heappop(nums)
  result += c1 + c2
  heapq.heappush(nums,c1+c2)

print(result)