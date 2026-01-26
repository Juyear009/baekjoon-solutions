import sys
from itertools import combinations

input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
house = []
chicken = []

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      house.append([i,j])
    elif graph[i][j] == 2:
      chicken.append([i,j])

answer = float('inf')

for comb in combinations(chicken,M):
  temp1 = 0
  for h in house:
    temp2 = float('inf')
    for c in comb:
      dist = abs(c[0]-h[0]) + abs(c[1]-h[1])
      temp2 = min(temp2,dist)
    temp1 += temp2
  answer = min(answer,temp1)

print(answer)