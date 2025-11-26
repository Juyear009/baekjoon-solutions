from itertools import combinations

def combination(arr):
  sums = []
  for i in range(len(arr)+1):
    for c in combinations(arr,i):
      sums.append(sum(c))
  return sums

N,C = map(int,input().split())
W = list(map(int,input().split()))

left = W[:N//2]
right = W[N//2:]

left_comb = combination(left)
right_comb = combination(right)

left_comb.sort()
right_comb.sort()

result = 0
p1 = 0
p2 = len(right_comb) - 1

while p1 < len(left_comb) and p2 >= 0:
  s = left_comb[p1] + right_comb[p2]
  if s <= C:
    result += p2 + 1
    p1 += 1
  else:
    p2 -= 1
print(result)