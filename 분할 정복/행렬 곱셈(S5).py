# 기본 풀이
def solved(array,idx):
  result = 0
  for i in range(M):
    result += array[i] * B[i][idx]
  return result


N, M = map(int, input().split())
A = []

for i in range(N):
  A.append(list(map(int,input().split())))

M, K = map(int, input().split())
B = []

for i in range(M):
  B.append(list(map(int,input().split())))

for i in A:
  for j in range(K):
    print(solved(i,j), end=" ")
  print()