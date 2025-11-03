def check(num):
  cnt = 0
  for i in range(1,N+1):
    cnt += min(num // i, N)
  
  return cnt < K

def binary_search():
  left = 1
  right = N * N
  while left <= right:
    mid = (left + right) // 2
    if check(mid):
      left = mid + 1
    else:
      right = mid - 1
  return left



N = int(input())
K = int(input())

print(binary_search())


# 1 2 3
# 2 4 6
# 3 6 9

# 1 2 2 3 3 4 6 6 9