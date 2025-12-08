from bisect import bisect_left, bisect_right

T = int(input())

n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

sumA = [0]
sumB = [0]

for i in range(n):
  sumA.append(sumA[-1] + A[i])

for i in range(m):
  sumB.append(sumB[-1] + B[i])

subA = []
subB = []

for i in range(n):
  for j in range(i+1,n+1):
    subA.append(sumA[j]-sumA[i])

for i in range(m):
  subB.append(sumB[i])
  for j in range(i+1,m+1):
    subB.append(sumB[j]-sumB[i])

subA.sort()
subB.sort()
result = 0

for i in subB:
  target = T - i
  left = bisect_left(subA,target)
  right = bisect_right(subA,target)
  result += right - left

print(result)