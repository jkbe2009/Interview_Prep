from collections import deque

class Node:
  def __init__(self, d):
    self.data = d
    self.left = None
    self.right = None
    
def print_tree(root):
  if root == None:
    return
    
  result = []
  q = deque()
  q.append(root)

  while q:
    node = q.popleft()
    if node is None:
      result.append(None)
      continue
    val = node.data
    result.append(val)
    left = node.left
    right = node.right
    q.append(left)
    q.append(right)
  print("Flat Tree:")
  cut_off = 0
  for i, val in enumerate(result):
    if val != None:
      cut_off = i+1
  print(result[:cut_off])
  return
  
def insert_BST_recursive(root, key):
  if root == None:
    return Node(key)

  if key == root.data:
    return root
  elif key < root.data:
    root.left = insert_BST_recursive(root.left, key)
  else:
    root.right = insert_BST_recursive(root.right, key)
  return root
  
def insert_BST_iterative(root, key):
  if root == None:
     return Node(key)
  curr = root
  
  while curr:
    if key == curr.data:
      return root
    elif key < curr.data:
      if curr.left == None:
        curr.left = Node(key)
        return root
      else:
        curr = curr.left
    else:
      if curr.right == None:
        curr.right = Node(key)
        return root
      else:
        curr = curr.right

  return root


root = None
print_tree(root)
input = [10,5,15,10,12,18,20,14]

for val in input:
  root = insert_BST_recursive(root, val)
print_tree(root)

root = None
print_tree(root)
for val in input:
  root = insert_BST_iterative(root, val)
print_tree(root)