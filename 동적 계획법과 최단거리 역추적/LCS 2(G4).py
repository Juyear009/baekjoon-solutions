word1 = input()
word2 = input()

dp = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]

for i in range(1,len(word2)+1):
  for j in range(1,len(word1)+1):
    if word2[i-1] == word1[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
print(dp)
i = len(word2)
j = len(word1)
lcs = []

while i > 0 and j > 0:
  if word2[i-1] == word1[j-1]:
    lcs.append(word2[i-1])
    i -= 1
    j -= 1
  else:
    if dp[i-1][j] > dp[i][j-1]:
      i -= 1
    else:
      j -= 1

print("".join(reversed(lcs)))