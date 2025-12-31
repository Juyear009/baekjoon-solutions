def solution(N,X):
  global res
  if X == 0:
    return 0
  if N == 0:
    return 1
  if X == 1:
    return 0
  elif X <= 1 + len[N-1]:
    return solution(N-1,X-1)
  elif X == 1 + len[N-1] + 1:
      return patty[N-1] + 1
  elif X <= 1 + len[N-1] + 1 + len[N-1]:
      return patty[N-1] + 1 + solution(N-1, X - (1 + len[N-1] + 1))
  else:
      return patty[N]


N, X = map(int, input().split())

len = [0] * (N+1)
patty = [0] * (N+1)

len[0] = 1
patty[0] = 1

for i in range(1, N+1):
    len[i] = len[i-1] * 2 + 3
    patty[i] = patty[i-1] * 2 + 1

print(solution(N,X))
