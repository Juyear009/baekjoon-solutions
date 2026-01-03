import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
  N,M = map(int,input().split())
  graph = [[] for _ in range(N+1)]
  for j in range(M):
    input()
  print(N-1)
