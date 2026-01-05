import sys

input = sys.stdin.readline

n1 = int(input())
w1 = list(map(int,input().split()))
n2 = int(input())
w2 = list(map(int,input().split()))

dp = [[False for _ in range(15001)] for _ in range(n1+1)]
dp[0][0] = True

for i in range(1,n1+1):
  w = w1[i-1]
  for d in range(15001):
    if dp[i-1][d]:
      dp[i][d] = True
      if w + d <= 15000:
        dp[i][w+d] = True
      dp[i][abs(w-d)] = True

result = []
for w in w2:
  if w <= 15000 and dp[n1][w]:
    result.append("Y")
  else:
    result.append("N")

print(" ".join(result))
