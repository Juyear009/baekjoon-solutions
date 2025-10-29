import sys

N, M = map(int,input().split())

dic = {}
sortedList = []

for i in range(N):
  word = sys.stdin.readline().strip()
  if len(word) >= M:
    if word in dic:
      dic[word][0] -= 1
    else:
      dic[word] = [99999,10-len(word)]

for i in dic:
  sortedList.append([dic[i][0], dic[i][1], i])

sortedList.sort()

for i in sortedList:
  sys.stdout.write(i[2] + "\n")