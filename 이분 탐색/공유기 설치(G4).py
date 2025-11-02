import sys

def check(length):
  cnt = 1
  temp = 0
  for i in range(1,len(x)):
    if x[i] - x[temp] >= length:
      cnt += 1
      temp = i
  return cnt >= C

def binary_search():
  left = 1
  right = x[-1] - x[0]
  while left <= right:
    mid = (left + right) // 2
    if check(mid):
      left = mid + 1
    else:
      right = mid - 1
  return right

input = sys.stdin.readline

N, C = map(int,input().split())
x = [int(input()) for _ in range(N)]

x.sort()

print(binary_search())