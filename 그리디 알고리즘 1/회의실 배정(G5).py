import sys

N = int(input())
times = []
result = []

for i in range(N):
  times.append(list(map(int,sys.stdin.readline().split())))

times.sort()

for t in times:
  if len(result) == 0:
    result.append(t)
  elif result[-1][1] > t[1]:
    result[-1] = t
  elif result[-1][1] <= t[0]:
    result.append(t)

print(len(result))