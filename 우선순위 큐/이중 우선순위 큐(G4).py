import heapq
import sys

T = int(input())
input = sys.stdin.readline

for _ in range(T):
  K = int(input())
  q1 = []
  q2 = []
  isDelete = set()
  for i in range(K):
    c,n = input().split()
    if c == "I":
      heapq.heappush(q1,[int(n),i])
      heapq.heappush(q2,[-int(n),i])
    elif c == "D":
      if n == "-1":
        while q1:
          num,idx = heapq.heappop(q1)
          if idx not in isDelete:
            isDelete.add(idx)
            break
      else:
        while q2:
          num,idx = heapq.heappop(q2)
          if idx not in isDelete:
            isDelete.add(idx)
            break
  
  max = -float('inf')
  min = float('inf')
  for i in q1:
    if i[1] not in isDelete:
      if i[0] > max:
        max = i[0]
      if i[0] < min:
        min = i[0]

  if max == -float('inf') or min == float('inf'):
    print("EMPTY")
  else:
    print(max,min)