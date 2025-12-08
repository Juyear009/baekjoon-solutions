
class Node():
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

def insert(root,val):
  if root == None:
    return Node(val)
  elif root.val < val:
    root.right = insert(root.right,val)
  elif root.val > val:
    root.left = insert(root.left,val)
  return root

def solve():
  pass