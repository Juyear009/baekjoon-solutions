import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

nums = [[] for _ in range(9)]
for i in range(9):
    t = input().rstrip()
    for j in t:
      nums[i].append(int(j))
v = []

row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
box = [[False]*10 for _ in range(9)]

def get_box(r, c):
    return (r // 3) * 3 + (c // 3)

for i in range(9):
    for j in range(9):
        if nums[i][j] == 0:
            v.append((i, j))
        else:
            val = nums[i][j]
            row[i][val] = True
            col[j][val] = True
            box[get_box(i, j)][val] = True


def sdoku(idx):
    if idx == len(v):
        for i in range(9):
            for j in nums[i]:
                print(j,end="")
            print()
        sys.exit()

    r, c = v[idx]
    b = get_box(r, c)

    for val in range(1, 10):
        if not row[r][val] and not col[c][val] and not box[b][val]:

            nums[r][c] = val
            row[r][val] = col[c][val] = box[b][val] = True

            sdoku(idx + 1)

            nums[r][c] = 0
            row[r][val] = col[c][val] = box[b][val] = False


sdoku(0)
