def solve(s1,e1,s2,e2):
  if s1 > e1 or s2 > e2:
    return
  
  root = postorder[e2]
  print(root, end=" ")

  idx = inorder.index(root)

  left = idx - s1

  solve(s1,idx-1,s2,s2+left-1)

  solve(idx+1,e1,s2+left,e2-1)

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

solve(0,n-1,0,n-1)