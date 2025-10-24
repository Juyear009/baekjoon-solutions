N,K = map(int,input().split())
t = list(map(int,input().split()))
sums = []

sums.append(sum(t[0:K]))

for i in range(K,N):
    sums.append(sums[-1] - t[i-K] + t[i])

print(max(sums))