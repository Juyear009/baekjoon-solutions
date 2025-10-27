def func1(start,end):
  result = 1
  for i in range(start,end+1):
    result *= i
  return result

T = int(input())

for i in range(T):
  N,M = map(int,input().split())
  C1 = func1(M+1-N, M)
  C2 = func1(1, N)
  print(C1//C2)