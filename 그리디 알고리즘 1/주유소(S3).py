N = int(input())
lengths = list(map(int,input().split()))
prices = list(map(int,input().split()))

result = 0
minPrice = prices[0]

for i in range(len(prices[:-1])):
  if prices[i] < minPrice:
    minPrice = prices[i]
  result += minPrice * lengths[i]

print(result)