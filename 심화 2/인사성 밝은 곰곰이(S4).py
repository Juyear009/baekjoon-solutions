import sys

N = int(input())
dic = {}
result = 0

for i in range(N):
  name = sys.stdin.readline().strip()
  if name == "ENTER":
    dic = {}
  elif name not in dic:
    result += 1
    dic[name] = True

print(result)