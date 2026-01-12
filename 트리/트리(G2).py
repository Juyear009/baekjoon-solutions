from collections import deque

def solution(inOrder):
  if len(inOrder) == 0:
    return
  if len(inOrder) == 1:
    print(inOrder[0],end=" ")
    preOrder.popleft()
    return
  root = preOrder.popleft()
  idx = inOrder.index(root)
  solution(inOrder[:idx])
  solution(inOrder[idx+1:])
  print(root,end=" ")

T = int(input())
for _ in range(T):
  n = int(input())
  preOrder = list(map(int,input().split()))
  preOrder = deque(preOrder)
  inOrder = list(map(int,input().split()))
  solution(inOrder)
  print()