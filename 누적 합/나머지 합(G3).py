N,M = map(int,input().split())
nums = list(map(int,input().split()))

prefix = 0
sumOfNums = [0 for _ in range(M)]
result = 0

for i in range(N):
    prefix = (prefix + nums[i]) % M
    if prefix == 0:
        result += 1
    sumOfNums[prefix] += 1

for num in sumOfNums:
    if num > 1:
        result += num * (num - 1) // 2

print(result)
            