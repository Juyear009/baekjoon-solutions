## class로 삽입 직접 구현

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# def insert(root,val):
#   if root is None:
#     return Node(val)
#   if val < root.val:
#     root.left = insert(root.left, val)
#   else:
#     root.right = insert(root.right, val)
#   return root

# def postorder(root):
#   if root != None:
#     postorder(root.left)
#     postorder(root.right)
#     sys.stdout.write(str(root.val) + "\n")


# root = None
# while True:
#   try:
#     N = int(input())
#     root = insert(root,N)
#   except:
#     break

# postorder(root)

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

pre = []

while True:
  try:
    pre.append(int(input()))
  except:
    break

def solve(start,end):
  if start > end:
    return
  
  root = pre[start]
  idx = start + 1
  while idx <= end and pre[idx] < root:
    idx += 1

  solve(start+1, idx-1)
  solve(idx,end)
  print(root)

solve(0,len(pre)-1)