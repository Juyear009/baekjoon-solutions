import sys
import heapq

T = int(input())

for i in range(T):
  M = int(sys.stdin.readline())
  nums = []
  result = []
  leftQueue = []
  rightQueue = []
  for _ in range((M + 9) // 10):
        nums += list(map(int,sys.stdin.readline().split()))

  for j in range(1,len(nums)+1):
    if not leftQueue or nums[j-1] <= -leftQueue[0]:
       heapq.heappush(leftQueue, -nums[j-1])
    else:
       heapq.heappush(rightQueue, nums[j-1])
    
    if len(leftQueue) > len(rightQueue) + 1:
       heapq.heappush(rightQueue, -heapq.heappop(leftQueue))
    elif len(rightQueue) > len(leftQueue):
       heapq.heappush(leftQueue, -heapq.heappop(rightQueue))
    if j % 2 == 1:
      result.append(-leftQueue[0])

  print(len(result))
  for i in range(len(result)):
    print(result[i], end=' ')
    if (i + 1) % 10 == 0:
       print()
  print()