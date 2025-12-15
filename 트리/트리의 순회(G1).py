import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0] * (n + 1)
for i, v in enumerate(inorder):
    pos[v] = i

def solve(s1, e1, s2, e2):
    if s1 > e1 or s2 > e2:
        return

    root = postorder[e2]
    print(root, end=' ')

    root_idx = pos[root]
    left_size = root_idx - s1

    solve(s1, root_idx - 1,
          s2, s2 + left_size - 1)

    solve(root_idx + 1, e1,
          s2 + left_size, e2 - 1)


solve(0, n - 1, 0, n - 1)
