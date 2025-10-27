import sys

s = input()
n = int(input())
dic = {}

for j in range(26):
    dic[chr(97+j)] = [0] * len(s)
    for i in range(len(s)):
        if s[i] == chr(97+j):
            dic[chr(97+j)][i] = (dic[chr(97+j)][i-1] + 1)
        else:
            dic[chr(97+j)][i] = (dic[chr(97+j)][i-1])

for i in range(n):
    a,l,r = sys.stdin.readline().split()
    if int(l) > 0:
        sys.stdout.write(str(dic[a][int(r)] - dic[a][int(l)-1]) + "\n")
    else:
        sys.stdout.write(str(dic[a][int(r)]) + "\n")