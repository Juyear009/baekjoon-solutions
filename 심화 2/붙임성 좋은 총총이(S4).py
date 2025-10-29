import sys

N = int(input())
dic = {"ChongChong" : True}
result = 0

for i in range(N):
  name1, name2 = sys.stdin.readline().strip().split()
  if name1 in dic:
    if dic[name1] == True:
      dic[name2] = True
  elif name2 in dic:
    if dic[name2] == True:
      dic[name1] = True

for i in dic:
  if dic[i] == True:
    result += 1

print(result)
