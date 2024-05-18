class Node:
  def __init__(self, d):
    self.data = d
    self.left = None
    self.right = None

def dfs_preorder(root):
  if root != None:
    print(root.data, end=" ")
    dfs_preorder(root.left)
    dfs_preorder(root.right)
  return

def dfs_inorder(root):
  if root != None:
    dfs_inorder(root.left)
    print(root.data, end=" ")
    dfs_inorder(root.right)
  return

def dfs_postorder(root):
  if root != None:
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.data, end=" ")
  return

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

print("\nPreorder Traversal:")
dfs_preorder(root)
print("\n\nInorder Traversal:")
dfs_inorder(root)
print("\n\nPostorder Traversal:")
dfs_postorder(root)