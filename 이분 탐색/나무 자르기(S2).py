def tree_length(h):
  total_length = 0
  for i in trees:
    if i - h > 0:
      total_length += i - h
  if total_length >= M:
    return True
  return False

def binary_search(trees):
  left = 1
  right = max(trees)
  while left <= right:
    mid = (left + right) // 2
    if tree_length(mid):
      left = mid + 1
    else:
      right = mid - 1
  return right

N, M = map(int,input().split())
trees = list(map(int,input().split()))

print(binary_search(trees))
