import sys
import heapq

input = sys.stdin.readline

N = int(input())
left = []
right = []

for i in range(N):
  num = int(input())
  if len(right) == 0 or right[0] >= num:
    heapq.heappush(left,-num)
  elif right[0] < num:
    heapq.heappush(right,num)

  if len(left) - 1 > len(right):
    t = heapq.heappop(left)
    heapq.heappush(right,-t)
  elif len(right) > len(left):
    t = heapq.heappop(right)
    heapq.heappush(left,-t)
  
  sys.stdout.write(str(-left[0]) + "\n")