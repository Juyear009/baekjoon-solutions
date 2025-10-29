# 브루트포스
N = int(input())

result = 0

if N % 5 == 0:
  result = N // 5
else:
  for i in range(N // 5 + 1):
    if (N - (5 * i)) % 3 == 0:
      result = i + ((N - (5 * i)) // 3)

if result == 0:
  print(-1)
else:
  print(result)

# 그리디 알고리즘
N = int(input())
result = 0

while N >= 0:
  if N % 5 == 0:
    result += N // 5
    print(result)
    break
  N -= 3
  result += 1
else:
  print(-1)

# 다이나믹 프로그래밍 맛보기
# dp[i-3] dp[i-5] 
# 마지막에 3kg 추가했다면 dp[i-3] + 1
# 마지막에 5kg 추가했다면 dp[i-5] + 1
# 작은 문제로 나누고 재사용 한다는 DP 알고리즘 만족