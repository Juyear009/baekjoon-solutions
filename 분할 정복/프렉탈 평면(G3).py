import sys

def solved(d,x,y):
  if x > R2 or x+d-1 < R1 or y > C2 or y+d-1 < C1: 
    return
  if d == 1:
    result[x-R1][y-C1] = 0
    return
  
  t = d//N
  for i in range(N):
    for j in range(N):
      if (N-K)//2 <= i < N-(N-K)//2 and (N-K)//2 <= j < N-(N-K)//2:
        pass
      else:
        solved(t,x+t*i,y+t*j)


s,N,K,R1,R2,C1,C2 = map(int,input().split())
result = [[1 for _ in range(C2-C1+1)] for _ in range(R2-R1+1)]
solved(N**s,0,0)

for nums in result:
  for n in nums:
    sys.stdout.write(str(n))
  sys.stdout.write("\n")