import math
import sys

def can_cut(length):
  cnt = 0
  for i in lan:
    cnt += i // length
  if cnt >= N:
    return True
  return False

def binary_search(lan):
  left = 1
  right = max(lan)
  while left <= right:
    mid = (left + right) // 2
    if can_cut(mid):
      left = mid + 1
    elif can_cut(mid) == False:
      right = mid - 1
  return right

input = sys.stdin.readline

K,N = map(int,input().split())
lan = [int(input()) for _ in range(K)]

print(binary_search(lan))

