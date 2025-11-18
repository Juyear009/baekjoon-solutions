import sys

input = sys.stdin.readline
N = int(input())
scores = []

for i in range(N):
  scores.append(int(input()))

scores.reverse()
dp = [0] * N
dp[0] = scores[0]

if N >= 1:
  dp[0] = scores[0]
if N >= 2:
  dp[1] = scores[0] + scores[1]

for i in range(2, N):
  dp[i] = max(dp[i-3] + scores[i-1], dp[i-2]) + scores[i]

print(dp[N-1])
print(dp)