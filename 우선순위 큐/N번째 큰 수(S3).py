import heapq
import sys

input = sys.stdin.readline

N = int(input())
q = []
maxNum = None

for i in range(N):
  temp = (list(map(int,input().split())))
  if maxNum == None:
    maxNum = max(temp)
    heapq.heappush(q,maxNum)
  for j in range(N):
    if temp[j] > maxNum:
      heapq.heappush(q,temp[j])
    if len(q) > N:
      heapq.heappop(q)

print(heapq.heappop(q))