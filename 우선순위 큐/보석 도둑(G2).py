import sys
import heapq

input = sys.stdin.readline

N,K = map(int,input().split())
q = []
re = []
bags = []

for i in range(N):
  M,V = map(int,input().split())
  heapq.heappush(q,(M,-V))

for i in range(K):
  bags.append(int(input()))

bags.sort()
result = 0

for bag in bags:
  while len(q) != 0 and q[0][0] <= bag:
    M,V = heapq.heappop(q)
    heapq.heappush(re,V)
  if len(re) != 0:
    result += -heapq.heappop(re)

print(result)