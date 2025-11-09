import sys

def checkStat(t1):
  t2 = []
  total1 = 0
  total2 = 0
  for i in t1:
    for j in t1:
      if i != j:
        total1 += stats[i][j]
  for i in range(N):
    if i not in t1:
      t2.append(i)
  for i in t2:
    for j in t2:
      total2 += stats[i][j]
  
  return abs(total1-total2)

def solution(t1,S):
  global result
  if len(t1) == N//2:
    temp = checkStat(t1)
    if temp < result:
      result = temp
    return
  for i in range(S,N):
    if i not in t1:
      if len(t1) < N//2:
        t1.append(i)
        solution(t1,i)
        t1.pop()


input = sys.stdin.readline

N = int(input())
stats = [list(map(int,input().split())) for _ in range(N)]

result = 10e6

solution([],0)
print(result)