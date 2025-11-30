C, N = map(int,input().split())

city = []
for i in range(N):
  w,v = map(int,input().split())
  city.append((v,w))

city.sort()
dp = [float('inf')] * (C + city[-1][0]+1)
dp[city[0][0]] = city[0][1]

for v,w in city:
  dp[v] = min(dp[v],w)

for i in range(city[0][0] + 1, C+city[-1][0]+1):
  for v,w in city:
    if i - v < 1:
      continue
    dp[i] = min(dp[i], dp[i-v] + w)

result = float('inf')
for i in range(C,C+city[-1][0]+1):
  if dp[i] != float('inf'):
    result = min(result,dp[i])
print(result)