import sys

input = sys.stdin.readline

N = int(input())
edges = [list(map(int,input().split())) for _ in range(N)]

dp = [0] * N

for i in range(1,N):
    for j in range(i):
        pass