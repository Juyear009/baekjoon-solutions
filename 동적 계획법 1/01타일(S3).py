def solution():
  N = int(input())

  dp = []
  if N >= 1:
    dp.append(1)
  if N >= 2:
    dp.append(2)

  for i in range(3,N+1):
    temp = dp[-1]
    dp[-1] = (dp[-1] + dp[-2]) % 15746
    dp[-2] = temp

  print(dp[-1])

solution()


# 100 001 111
# 1100 1001 0011 1111
# 0011 0000 1001 1100 1111
# 10011 00111 10000 00001 11100 11001 11111