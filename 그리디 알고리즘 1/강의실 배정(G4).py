import sys
import heapq

input = sys.stdin.readline

N = int(input())
times = []
room = []

for i in range(N):
  s,t = map(int,input().split())
  times.append((s,t))

times.sort()

heapq.heappush(room,times[0][1])
res = 1

for i in range(1,N):
  if times[i][0] >= room[0]:
    heapq.heappop(room)
    heapq.heappush(room, times[i][1])
  else:
    heapq.heappush(room,times[i][1])
    if len(room) > res:
      res = len(room)

print(res)
