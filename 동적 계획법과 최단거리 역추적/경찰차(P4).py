import sys

input = sys.stdin.readline

N = int(input())
W = int(input())
dp = [[float('inf'),float('inf')] for _ in range(W)]
x,y = map(int,input().split())
dp[0][0] = abs(x-1) + abs(y-1)
dp[0][1] = abs(x-N) + abs(y-N)
c1 = [(x,y),(N,N)]
c2 = [(1,1),(x,y)]
r1 = [1]
r2 = [2]
for i in range(1,W):
    x,y = map(int,input().split())
    if dp[i-1][0] + abs(x-c1[0][0]) + abs(y-c1[0][1]) < dp[i-1][0] + abs(x-c1[1][0]) + abs(y-c1[1][1]):
        dp[i][0] = dp[i-1][0] + abs(x-c1[0][0]) + abs(y-c1[0][1])
        c1[0] = (x,y)
        r1.append(1)
    else:
        dp[i][0] = dp[i-1][0] + abs(x-c1[1][0]) + abs(y-c1[1][1])
        c1[1] = (x,y)
        r1.append(2)
    if dp[i-1][1] + abs(x-c2[0][0]) + abs(y-c2[0][1]) < dp[i-1][1] + abs(x-c2[1][0]) + abs(y-c2[1][1]):
        dp[i][1] = dp[i-1][1] + abs(x-c2[0][0]) + abs(y-c2[0][1])
        c2[0] = (x,y)
        r2.append(1)
    else:
        dp[i][1] = dp[i-1][1] + abs(x-c2[1][0]) + abs(y-c2[1][1])
        c2[1] = (x,y)
        r2.append(2)
print(dp)
if dp[-1][0] < dp[-1][1]:
    print(dp[-1][0])
    for i in r1:
        print(i)
else:
    print(dp[-1][1])
    for i in r2:
        print(i)